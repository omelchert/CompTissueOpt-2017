""" main_estimatePi_siSaStats.py

script for simple sampling MC strategy to determine PI
WITH STATISTICAL SUMMARY MEASURES 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
import numpy as np
from estimatePi import simpleSampling
from rngSwitch import fetchPRNG
from stats import basicStatistics

def main():
    N = int(sys.argv[1])  
    M = int(sys.argv[2])
    mode = sys.argv[3]
    
    av, sDev, sErr = basicStatistics(
        [simpleSampling(fetchPRNG(mode,seed),N) 
        for seed in np.random.randint(10**10,size=M)])

    print "# SIMPLE SAMPLING MC INTEGRATION:"
    print "# ", sys.argv[1:] 
    print av, sErr
    
main()
# EOF: main_estimatePi_siSaStats.py
