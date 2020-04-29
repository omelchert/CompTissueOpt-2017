""" main_estimatePi_simpleSampling.py

script for simple sampling MC strategy to determine PI

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
import math
from estimatePi import simpleSampling
from rngSwitch import fetchPRNG

def main():
    N = int(sys.argv[1])  
    seed = int(sys.argv[2])
    mode = sys.argv[3]
    rng = fetchPRNG(mode, seed)

    pi = simpleSampling(rng, N)

    print "# SIMPLE SAMPLING MC INTEGRATION:"
    print "# ", sys.argv[1:] 
    print "# estimate:", pi
    print "# exact:", math.pi
    
main()
# EOF: main_estimatePi_simpleSampling.py
