""" main_randomnessTest_unitVectors.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-24
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
import scipy.stats
from randomVariateGenerator import UnitSphere
from unitVectorTest import RandomnessTest


def main():
    # SIMULATION PARAMETERS
    N = int(sys.argv[1])        # number of samples
    M = int(sys.argv[2])        # number of runs
    a = 0.20                    # siginificance test
    nBins = 20                  # number of bins for pdf discretization
    sampler = UnitSphere()      # unit vector sampler

    # INITIALIZE TEST 
    myTest = RandomnessTest(sampler, N, M)

    # DUMP RESULTS 
    myTest.pdf(nBins)
    myTest.checkRandomness(a)

main()
# EOF: main_randomnessTest_unitVectors.py
