""" main_1DRW_endpointPMF.py

script for Monte Carlo sampling of 1D random walk endpositions
and statistical summary via pmf

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
from randomWalker1D import *
from rngSwitch import fetchPRNG
from pmf import PMF


def main():
    # PARSE COMMANDLINE ARGUMENTS 
    N = int(sys.argv[1])  # NUMBER OF STEPS 
    M = int(sys.argv[2])  # NUMBER OF WALKS
    mode = sys.argv[3]    # PRNG MODE

    # INITIALIZE STEP SAMPLER 
    sampler = StepSampler(fetchPRNG(mode))
    
    # INITIALIZE PMF TO ACCUMULATE ENDPOINTS
    pmf = PMF()
  
    # MC SIMULATION TO SAMPLE ENDPOINTS
    for m in range(M):
        rw = RandomWalker1D(0.0, sampler.discreteSymmetric)
        rw.walk(N)
        pmf.add(rw.x)

    # WRITE DATA TO STDOUT
    pmf.dump()
        
main()
# EOF: main_1DRW_endpointPMF.py
