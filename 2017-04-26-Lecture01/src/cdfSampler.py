""" cdfSampler.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-25
AUTHOR: O. Melchert
"""
import bisect
import random
import numpy as np

class CDFSampler(object):
     """Class implementing cdf sampler 
 
     Implements methods to sample the inverse of the provided cdf by building
     on the procedures outlined in Ref. [1]
 
     Notes:
         - if the cdf can be inverted by analytic means use the transformation
           method instead
 
     Refs:
         [1] Think Stats - Probability and Statistics for Programmers 
             Downey, A. B.
             O'Reilley, 2011 
     """
     def __init__(self, us, ps, r=random.random):
         """initializes instance of cdf sampler

         Args:
             us (array) list of sampled x points
             ps (array) list of probabilities with same length as us
             r (object) random number generator (default: random.random)
         """
         self.us = us
         self.ps = ps
         self.r  = r
     
     def value(self,p):
         """value of inverse cdf

         For a given probability p, returns the corresponding x-value

         Args:
             p (float) probability for which to compute inverse cdf

         Notes:
             - efficient implementation based on bisection algorithm
             - superceeds naive linear search, as, e.g. used by Ref. [1]

         Refs:
             [1] Diffuse radiation in the galaxy
                 Henyey, L.G. and Greenstein, J.L.
                 Astrophysical Journal, 93 (1941) 70
         """
         if p == 0: idx = 0
         if p == 1: idx = -1
         idx = bisect.bisect(self.ps,p)
         if p == self.ps[idx-1]: idx = idx-1
         return self.us[idx]

     def generate(self):
        """generates random variate

        Implements method to sample the inverse of the provided cdf 

        Returns:
            x (float): random variate sampled from pdf that yield given cdf
        """
        return self.value(self.r())

     def dump(self):
        for u, p in zip(self.us,self.ps):
            print u, p


def getCDFSampler(sList,r=random.random):
    """get cdf sampler

    Construct approximate cdf from provided list of unsorted (u,p(u)) pairs
    and yield a sampler that allows to generated random variates by numerical
    inversion 

    Args:
        sList (2-tuple list, floats) unsorted list of (u,p(u)) pairs
        r (object) random number generator (default: random.random)

    Returns:
        s (object) sampler generating random numbers by uniformly sampling 
            from cdf and performing numerical inversion via fast bisection 
    """
    u, p = zip(*sorted(sList))
    pCumSumNorm = np.cumsum(p)/np.sum(p)
    return CDFSampler(u,pCumSumNorm,r)

# EOF: cdfSampler.py 
