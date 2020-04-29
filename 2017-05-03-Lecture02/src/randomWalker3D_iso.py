""" randomWalker3D_iso.py

module implementing 3D random walker

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-02
AUTHOR: O. Melchert
"""
import random
from randomVariateGenerator import UnitSphere

class RandomWalker3D_iso(object):
    """isotropic random walker in 3D space"""
    def __init__(self, r=random.random, x0=(0,0,0), w0=(0,0,1) ):
        """instance of 1D random walker class

        Args: 
            x0 (3-tuple, floats) starting point of walk (default: x0=(0,0,0))
            w0 (3-tuple, floats) ini directional cosines (default: w0=(0,0,1))
            r (function) random number generator

        Attrib:
            x (3-tuple, float) current walker position
            w (3-tuple, float) current directional cosines
            nSteps (int) number of steps taken
            wSamp (object) directional cosine sampler
        """
        self.x0 = x0
        self.w = w0
        self.x  = x0
        self.nSteps = 0
        self.wSamp  = UnitSphere(r).generate

    def step(self):
        """perform single step
        """
        ux, uy, uz = self.x
        wx, wy, wz = self.w  
       
        self.x = (ux+wx, uy+wy, uz+wz)
        self.w = self.wSamp()
        self.nSteps += 1



# EOF: randomWalker3D_iso.py
