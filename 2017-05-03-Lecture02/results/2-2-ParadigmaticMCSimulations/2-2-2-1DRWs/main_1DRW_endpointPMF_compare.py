""" main_1DRW_endpointPMF_compare.py

script for Monte Carlo sampling of 1D random walk endpositions

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
import math
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


def p(x,N):
    """asymptotic Bernoulli distribution 

    Implements asymptotic form of endpoint distribution for discrete 
    symmetric random walk following Eq. (12) of Ref. [1]

    Args:
        m (int) endposition
        N (int) walk length
   
    Returns:
        WmN (float) probability of finding N step walk at endpoint m

    Notes:
        - approximation uses Stirlings formula and is valid in the limit
          N to infty and where x << N

    Refs:
        [1] Stochastic Problems in Physics and Astronomy
            Chandrasekhar, S
            Rev. Mod. Phys., 15 (1953) 1
            
    """
    return math.sqrt(2/math.pi/N)*math.exp(-x*x/2/N)

def main():
    # PARSE COMMANDLINE ARGUMENTS 
    N = int(sys.argv[1])  # NUMBER OF STEPS 
    M = int(sys.argv[2])  # NUMBER OF WALKS
    mode = sys.argv[3]

    # INITIALIZE STEP SAMPLER 
    sampler = StepSampler(fetchPRNG(mode))
    
    # INITIALIZE PMF TO ACCUMULATE ENDPOINTS
    pmf = PMF()
  
    # MC SIMULATION TO SAMPLE ENDPOINTS
    for m in range(M):
        rw = RandomWalker1D(0.0, sampler.discreteSymmetric)
        rw.walk(N)
        pmf.add(rw.x)

    # WRITE SIMULATION SUMMARY TO STDOUT
    print "# (x) (f(x)) (p(x)) (W(x,N)) (p(x,N))"
    for (k,v) in sorted(pmf.pmf.items()):
        print k, v, float(v)/pmf.n, W(k,N), p(k,N)
        
main()
# EOF: main_1DRW_endpointPMF_compare.py
