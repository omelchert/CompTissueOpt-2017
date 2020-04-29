""" randomVariateGenerator.py

Module implementing various random number generators that yield non-uniformly
distributed pseudo random numbers.

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017
"""
import random
from math import sqrt, sin, cos, pi, acos, exp, log


class ExpoVariate(object):
    """Class implementing sampler for exponential pdf 
    """
    def __init__(self, mu=1.0, r=random.random):
        """initializes instance of Expovariate sampler 

        Args:
            mu (float) scale parameter for exponential pdf (default = 1.0)
            r (generator): random number generator (default = random.random)

        Attrib:
            cdf (object) cumulative distribution function 
            icdf (object) inverse cdf
        """
        self.r = r
        self.mu = mu
        self.cdf = lambda x: 1.-exp(-x*mu)
        self.icdf = lambda x: -log(1.-x)/mu

    def generate(self):
        """generate random variate

        Uses transformation method for directly sampling from exponential pdf
        
        Returns:
            x (float) expovariate

        Notes:
            sampling strategy uses transformation method
        """
        return self.icdf(self.r())


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


# EOF: randomVariateGenerator.py
