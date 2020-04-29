""" main_1DRW_endpointPMF_chi2.py

script for Monte Carlo sampling of 1D random walk endpositions
and chi2 hypothesis testing

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
import math
import scipy.stats
from randomWalker1D import *
from rngSwitch import fetchPRNG
from pmf import PMF


def W(m,N):
    """Bernoulli distribution 

    Implements exact solution of endpointdistribution for discrete 
    symmetric random walk following Eq. (3) of Ref. [1]

    Args:
        m (int) endposition
        N (int) walk length
   
    Returns:
        WmN (float) probability of finding N step walk at endpoint m


    Refs:
        [1] Stochastic Problems in Physics and Astronomy
            Chandrasekhar, S
            Rev. Mod. Phys., 15 (1953) 1
            
    """
    fac = lambda x: math.factorial(x)
    return pow(0.5,N)*fac(N)/fac((N+m)/2)/fac((N-m)/2)


def chiSquareTest((N,M),pmf):
    """chi square test

    Implements chi square test for 1D random walk by comparing expected
    frequency obtained from exact Bernoullian endpoint distibution to 
    observed frequencies

    Notes:
        - chi-square test for 1D random walk tests null hypothesis:
          "the sampled endpoints are from a population of Bernoullian 
          distributed random variables"

    Args:
        pmf (dict) dictionary containing (resultant, frequency) pairs

    Returns:
        nothing, but dumps test summary to stdout
    """
    # TEST PREPROCESSING:
    # (1) OBTAIN OBSERVED AND EXPECTED FREQUENCIES 
    fObs = [v for (k,v) in sorted(pmf.pmf.items())]
    fExp = [int(M*W(k,N)) for (k,v) in sorted(pmf.pmf.items())]
    # (2) RESTRICT TEST TO CATEGORIES WITH FREQUENCY AT LEAST 5 
    datSet = zip(fObs,fExp)
    filteredSet = filter(lambda x: x[0] > 5, datSet)
    fObs, fExp = zip(*filteredSet)

    # PERFORM CHI-SQUARE TEST
    (stats, pValue) = scipy.stats.chisquare(fObs,fExp)
    
    # DUMP TEST SUMMARY TO STDOUT
    print "# TEST NULL HYPOTHESIS FOR SETUP:"
    print "#", sys.argv[:]
    print "# CHI2-stats:", stats
    print "# p-Value: ", pValue
    print "# TEST RESULT: ", "PASSED" if pValue>=0.05 else "FAILED"

def main():
    # PARSE COMMANDLINE ARGUMENTS 
    N = int(sys.argv[1])  # NUMBER OF STEPS 
    M = int(sys.argv[2])  # NUMBER OF WALKS
    mode = sys.argv[3]

    # INITIALIZE STEP SAMPLER 
    sampler = StepSampler(fetchPRNG(mode,7))
    
    # INITIALIZE PMF TO ACCUMULATE ENDPOINTS
    pmf = PMF()
  
    # MC SIMULATION TO SAMPLE ENDPOINTS
    for m in range(M):
        rw = RandomWalker1D(0.0, sampler.discreteSymmetric)
        rw.walk(N)
        pmf.add(rw.x)

    chiSquareTest((N,M),pmf) 
        
main()
# EOF: main_1DRW_endpointPMF_chi2.py
