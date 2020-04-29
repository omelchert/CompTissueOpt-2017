""" irradiationSource.py

module implementing various irradiation sources 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-16
AUTHOR: O. Melchert
"""
import numpy as np
import random


class Beam(object):
    """Class implementing simple beam
    """
    def __init__(self, a0):
        """instance of simple beam class

        Args:
            a0 (float) beam radius
        """
        self.a0 = a0

    def iniPos(self):
        """initial photon position

        Implements inversion method to sample photon position in beam of 
        given radius

        Returns:
            x0, y0, z0 (3-tuple, float) intial photon packet position
        """
        r0 = self.a0*np.sqrt(random.random())
        p0 = 2*np.pi*random.random()
        return r0*np.cos(p0), r0*np.sin(p0), 0.

    def iniDirCos(self):
        """initial directional cosine

        Implements initial directional cosine

        Returns:
            wx, wy, wz (3-tuple, float) initial directional cosines
        """
        return 0, 0, 1



class Fiber(object):
    """Class implementing realisic fiber 
    """
    def __init__(self, a0, NA, nf, nm):
        """instance of realistic fiber

        Args:
            a0 (float) beam radius
            NA (float) numerical aperture
            nf (float) index of fiber
            nm (float) index of medium
        """
        self.a0 = a0
        self.NA = NA
        self.nf = nf
        self.nm = nm

    def iniPos(self):
        """initial photon position

        Implements inversion method to sample photon position in beam of 
        given radius

        Returns:
            x0, y0, z0 (3-tuple, float) intial photon packet position
        """
        r0 = self.a0*np.sqrt(random.random())
        p0 = 2*np.pi*random.random()
        return r0*np.cos(p0), r0*np.sin(p0), 0.

    def iniDirCos(self):
        """initial directional cosine

        Implements initial directional cosine wherein z-component is 
        restricted to lie within the limites set by the numerical 
        aperture of the fiber, see Ref. [1]

        Returns:
            wx, wy, wz (3-tuple, float) initial directional cosines

        Refs:
            [1] Influence of the scattering phase function on light
                transport measurements in turbid media performed with
                small source-detector separations
                Mourant, J and Boyer, J and Hielscher, A. and Bigio, I.
                Optics Letters, 21 (1996) 546
        """
        wz = np.cos(np.arcsin(self.NA*self.nf/self.nm)*random.random())
        p1 = 2*np.pi*random.random()
        fac = np.sqrt(1.-wz*wz)
        return fac*np.cos(p1), fac*np.sin(p1), wz


# EOF: irradiationSource.py
