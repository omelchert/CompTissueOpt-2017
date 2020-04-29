""" randomWalker1D.py

module implementing simple 1D random walker

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import random


class StepSampler(object):
    def __init__(self, r=random.random):
        self.r = r

    def discreteSymmetric(self):
        """discrete symmetric step size sampler

        Returns:
            dx (int) discrete random variable 
                uniformly taken from [-1,1]
        """
        return 1 if self.r() < 0.5 else -1 


class RandomWalker1D(object):
    def __init__(self, x0=0., r = StepSampler().discreteSymmetric):
        """instance of 1D random walker class

        Args: 
            x0 (float) starting point of the walk (default: x0=0.)
            r (function) step sampler (default: discrete sample space [-1,1])

        Attrib:
            x (float) current walker position
            nSteps (int) number of steps taken
        """
        self.x0 = x0
        self.x  = x0
        self.nSteps = 0
        self.r  = r 

    def step(self):
        """perform single step
        """
        self.x += self.r()
        self.nSteps += 1

    def walk(self, N=1):
        """perform walk
        
        performs a walk consisiting of consequtive steps 

        Args:
            N (int) number of steps in walk (default: 1)

        Returns:
            x (float) endpoint after N steps
        """
        for i in range(N):
            self.x += self.r()
        self.nSteps += N
        return float(self.x)


# EOF: randomWalker1D.py
