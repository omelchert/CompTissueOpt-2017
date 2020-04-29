""" main_1DRW.py

script for simple 1D random walk

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
from randomWalker1D import *
from rngSwitch import fetchPRNG

def main():
    # PARSE COMMANDLINE ARGUMENTS 
    N = int(sys.argv[1])  # NUMBER OF STEPS 
    seed = int(sys.argv[2])
    mode = sys.argv[3]

    # INITIALIZE STEP SAMPLER 
    sampler = StepSampler(fetchPRNG(mode,seed))

    # INITIALIZE RANDOM WALKER AT ORIGIN
    rw = RandomWalker1D(0.0, sampler.discreteSymmetric)

    # SINGLE MC SIMULATION
    for i in range(N):
        print rw.nSteps, rw.x
        rw.step()

main()
# EOF: main_1DRW.py
