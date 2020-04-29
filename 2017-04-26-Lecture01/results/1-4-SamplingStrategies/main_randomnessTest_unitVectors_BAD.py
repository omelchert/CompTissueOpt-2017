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
from linearCongruentialGenerator import LCG


def main():
    # SIMULATION PARAMETERS
    N = int(sys.argv[1])        # number of samples
    M = int(sys.argv[2])        # number of runs
    alpha = 0.20                    # siginificance test
    nBins = 20                  # number of bins for pdf discretization

    seed = 323.
    a, c, m = 106, 1283, 6075 

    # INITIALIZE INSTANCE OF PRNG
    r = LCG(a, c, m, seed/m)

    # INITIALIZE INSTANCE OF UNIT SPHERE SAMPLER
    sampler = UnitSphere(r.next)

    # INITIALIZE TEST 
    myTest = RandomnessTest(sampler, N, M)

    # DUMP RESULTS 
    myTest.pdf(nBins)
    myTest.checkRandomness(alpha)

main()
# EOF: main_randomnessTest_unitVectors.py
