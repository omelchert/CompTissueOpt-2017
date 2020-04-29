""" photonPacket3D.py

module implementing 3D random walker to model photon migration in media

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-02
AUTHOR: O. Melchert
"""
import random
import numpy as np


class PhotonPacket(object):
    """random walker in 3D space"""
    def __init__(self, sSamp, wSamp, x0=(0,0,0), w0=(0,0,1) ):
        """instance of 3D random walker class

        Args: 
            x0 (3-tuple, floats) starting point of walk (default: x0=(0,0,0))
            w0 (3-tuple, floats) ini directional cosines (default: w0=(0,0,1))
            wSamp (function) directional cosine sampler
            sSamp (function) stepsize sampler

        Attrib:
            x (3-tuple, float) current walker position
            w (3-tuple, float) current directional cosines
            nSteps (int) number of steps taken
            E (float) current photon packet weight
            dE (float) last weight decrement
        """
        self.x0 = x0
        self.w = w0
        self.x  = x0
        self.nSteps = 0
        self.sSamp  = sSamp 
        self.wSamp  = wSamp 
        self.E = 1.
        self.dE = 0.


    def propagate(self):
        """perform single propagation step

        Implements single propagation step for 3D photon migration by 
        computing new stepsize, followed by translation and computing new 
        directions for the next step

        Notes:
            - single step cosists of two elementary events: 
              absorption and scattering

            - proper modeling of photon migration:
              
              stepsize sampling: use ExpoVariate()
                  implements variable step size method to model 
                  light propagation in medium, wherein probability
                  density of packet stepsize s is given by

                   p(s) = (\mu_a+\mu_s) \exp{-(\mu_a+\mu_s)s}
                  
                  Sampling s this way is equivalent to say that
                  a photon is forced to be absorbed or scattered
                  after each step with no interaction along the
                  propagated distance (NOTE: small s have high p(s)),
                  see module randomVariateGenerator.py and Ref [1]

              directional cosine samping: use HenyeyGreenstein()
                  samples Henyey-Greenstein phase function, see 
                  module randomVariateGenerator.py and Ref [2]

        Refs:
            [1] A Monte Carlo Model of light propagation in tissue
                Prahl, S. and Keijzer, M. and Jacques, S. and Welch, A. 
                Proc. SPIE IS, 5 (1989) 102
                
            [2] Multiple Scattering in Reflection Nebulae
                Witt, A. N.
                Astrophys. J., 35 (1977) 1
        """
        ux, uy, uz = self.x
        wx, wy, wz = self.w  
        sinTcosP, sinTsinP, cosT = self.wSamp()
        s = self.sSamp()

        if abs(wz) < 0.99999:
            fac = 1./np.sqrt(1.- wz*wz)
            wxp = wx*cosT - fac*(wy*sinTcosP - wx*wz*sinTsinP)
            wyp = wy*cosT + fac*(wx*sinTcosP + wy*wz*sinTsinP)
            wzp = wz*cosT - sinTsinP*np.sqrt(1-wz*wz)
        else:
            wxp = sinTcosP
            wyp = sinTsinP 
            wzp = cosT*wz
       
        self.x = (ux+s*wx, uy+s*wy, uz+s*wz)
        self.w = (wxp, wyp, wzp)
        self.nSteps += 1

    def absorb(self,a):
        """absorption 

        Implements partial absorption of photon energy after 
        elementary propagation step, see Ref [1].

        Args:
            a (float) single particle albedo

        Notes:
            - After a propagation step, the photon packet is split
              into two parts. One part is scattered, i.e. redirected
              and moved (see method step()), the other part is absorbed. 
              Therefore, the  weight of the photon packet after the ith 
              scattering event is decreased according to the Beer-Lambert 
              law for turbid media:
              w_{i+1} = w_i (1-frac{\mu_s}{\mu_s+\mu_a})
              where frac{\mu_s}{\mu_s+\mu_a} is the single particle albedo

        Refs:
            [1] A Monte Carlo Model of light propagation in tissue
                Prahl, S. and Keijzer, M. and Jacques, S. and Welch, A. 
                Proc. SPIE IS, 5 (1989) 102
        """
        dE = (1.-a)*self.E
        self.dE = dE
        self.E -= dE


    def exists(self,pm=0.1):
        """check whether to propagate further

        Implements roulette strategy to determine whether to propagate photon
        packet further

        Args:
            pm (float) packet survival probability

        Returns:
            flag (bool) False only if photon is terminated

        Note:
            - roulette technique gives a photon a chance of surviving with
              probabilty pm and weight self.E/pm or else its weight is set
              to zero.  This means that for, say, pm=0.1, a photon packet is
              terminated 9 out of 10 times, but once it is kept with a weight
              that is increase by a factor of 10. Hence, packets are
              terminated most of the time but energy is conserved by
              occationally keeping packets with increased weight.  This
              removes the photon in an unbiased fashion without violating
              energy conservation and without propagating a packet with
              negligible weight. See Ref [1].

            - photon should not be propagated further as soon as the method
              returns the boolean flag False for the first time 

        Refs:
            [1] A Monte Carlo Model of light propagation in tissue
                Prahl, S. and Keijzer, M. and Jacques, S. and Welch, A. 
                Proc. SPIE IS, 5 (1989) 102
        """
        def _roulette(pm):
           if random.random() < pm:
                self.E /= pm
                myState = True
           else: 
                myState = False
           return myState

        return True if self.E > 1e-3 else _roulette(pm) 

    def __str__(self):
        ux, uy, uz = self.x
        wx, wy, wz = self.w  
        return "%lf  %lf %lf %lf %lf %lf %lf  %lf"\
            %(self.E, np.sqrt(ux*ux+uy*uy+uz*uz), ux, uy, uz, wx, wy, wz) 
            



# EOF: randomWalker3D.py
