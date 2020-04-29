""" randomWalker3D.py

module implementing 3D random walker

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-02
AUTHOR: O. Melchert
"""
import random
import numpy as np


class RandomWalker3D(object):
    """random walker in 3D space"""
    def __init__(self, wSamp, x0=(0,0,0), w0=(0,0,1) ):
        """instance of 3D random walker class

        Args: 
            x0 (3-tuple, floats) starting point of walk (default: x0=(0,0,0))
            w0 (3-tuple, floats) ini directional cosines (default: w0=(0,0,1))
            wSamp (function) directional cosine sampler

        Attrib:
            x (3-tuple, float) current walker position
            w (3-tuple, float) current directional cosines
            nSteps (int) number of steps taken
        """
        self.x0 = x0
        self.w = w0
        self.x  = x0
        self.nSteps = 0
        self.wSamp  = wSamp 

    def step(self):
        """perform single step

        Implements single step for 3D random walker by computing new 
        directions following Ref [1]

        Refs:
            [1] Multiple Scattering in Reflection Nebulae
                Witt, A. N.
                Astrophys. J., 35 (1977) 1
        """
        ux, uy, uz = self.x
        wx, wy, wz = self.w  
        sinTcosP, sinTsinP, cosT = self.wSamp()
       
        if abs(wz) < 0.99999:
            fac = 1./np.sqrt(1.- wz*wz)
            wxp = wx*cosT - fac*(wy*sinTcosP - wx*wz*sinTsinP)
            wyp = wy*cosT + fac*(wx*sinTcosP + wy*wz*sinTsinP)
            wzp = wz*cosT - sinTsinP*np.sqrt(1-wz*wz)
        else:
            wxp = sinTcosP
            wyp = sinTsinP 
            wzp = cosT*wz
       
        self.x = (ux+wx, uy+wy, uz+wz)
        self.w = (wxp, wyp, wzp)
        self.nSteps += 1


# EOF: randomWalker3D.py
