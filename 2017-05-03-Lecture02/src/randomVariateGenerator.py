""" randomVariateGenerator.py

Module implementing various random number generators that yield non-uniformly
distributed pseudo random numbers.

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017
"""
import random
import cdfSampler
from math import sqrt, sin, cos, pi, acos


class UnitSphere(object):
    """Class implementing uniform sampling from surface of unit 3-sphere
    """
    def __init__(self,r=random.random):
        """initializes instance of UnitSphere class

        Args:
            r (generator): random number generator (default = random.random)
        """
        self.r = r

    def generate(self):
        """generates random variate

        Implements Marsaglias acceptance rejection method for uniformly
        sampling from the surface of the unit 3-sphere as discussed in Ref. [1]

        Returns:
            (Z1, Z2, Z3) (3-tuple, floats): uniformly sampled point on the 
                surface of the 3-sphere, i.e. the directional cosines

        Notes:
            sampling strategy uses acceptance rejection method

            implements Marsaglias 'new method' discussed in Ref. [1]

        Refs:
            [1] Choosing a point from the surface of a sphere
                Marsaglia, G.
                The Annals of Mathematical Statistics, 43 (1972) 645
        """
        x1 = x2 = 1.
        while(x1*x1 + x2*x2 >= 1):
            x1 = 2.*self.r() - 1.
            x2 = 2.*self.r() - 1.

        t = x1*x1 + x2*x2
        fac = sqrt(1.-t)
        return 2.*x1*fac, 2.*x2*fac, 1.-2.*t


class HenyeyGreenstein(object):
    """Class implementing uniform sampling from surface of unit 3-sphere
    """
    def __init__(self, g, r=random.random, MING=1e-3):
        """initializes instance of UnitSphere class

        Args:
            g (float): scattering anisotropy parameter in range (-1,1)
            r (generator): random number generator (default = random.random)
            MING (float): limit for approximate expansion (default: MING=1e-3)
        """
        self.g = g
        self.r = r
        self.MING = MING 

    def generate(self):
        """generates random variate

        Implements transformation method for sampling from Henyey-Greenstein
        phase function described in Ref. [1]. 

        Returns:
            (Z1, Z2, Z3) (3-tuple, floats): random variate sampled from 
                Henyey-Greenstein phase function 

        Notes:
            sampling strategy uses transformation method

            Z3 corresponds to cos(theta)

        Refs:
            [1] Diffuse radiation in the galaxy
                Henyey, L.G. and Greenstein, J.L.
                Astrophysical Journal, 93 (1941) 70
        """
        s = 2.*self.r()-1.
        g = self.g

        if abs(g) < self.MING: 
            mu = s + 3.*g*(1-s*s)/2 - 2.*g*g*s*(1-s*s) 
        else:
            mu = (1. + g*g - ((1.-g*g)/(1.+g*s))**2)/2./g

        fac = sqrt(1-mu*mu)
        phi = pi*(2*self.r()-1)
        cosPhi = cos(phi)
        sinPhi = sqrt(1.-cosPhi*cosPhi) if phi >= 0 else -sqrt(1.-cosPhi*cosPhi)
        return fac*cosPhi, fac*sinPhi, mu


class Irvine(object):
    def __init__(self,f,g1,g2,N,r=random.random):
        
        _pHG = lambda mu, g: ((1 - g*g)/(1 + g*g - 2*g*mu)**(3./2))/2
        
        self.r = r
        self.pI = lambda mu: f*_pHG(mu,g1) + (1.-f)*_pHG(mu,g2)
        self.cdfSampler = cdfSampler.getCDFSampler(self._sample(N))


    def _prob(self,u):
        return self.pI(u)

    def _sample(self,N):
        tup = lambda u: (u, self._prob(u))
        return [tup(2*self.r()-1) for i in range(N)]

    def generate(self): 
        phi = pi*(2*self.r() - 1)
        mu = self.cdfSampler.generate()
        fac = sqrt(1-mu*mu)
        return fac*cos(phi), fac*sin(phi), mu 

# EOF: randomVariateGenerator.py
