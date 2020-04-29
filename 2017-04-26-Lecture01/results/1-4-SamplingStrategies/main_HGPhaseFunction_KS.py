import sys; sys.path.append('../../src/')
from randomVariateGenerator import * 
import scipy.stats
import numpy as np


def F(g,u):
    return (1-g*g)*( 1./np.sqrt(1+g*g-2*g*u) - 1./(1+g)  )/2/g 

def main():

    N = int(sys.argv[1])
    Dcrit = 1.628/np.sqrt(N) 
    g, dg = 0.05, 0.05

    while g < 0.95:
        cdf = lambda x: F(g,x)
        myGen = HenyeyGreenstein(g)
        uList = sorted([myGen.generate()[2] for i in range(N)])

        D,p = scipy.stats.kstest(uList,cdf)
        print "g = %3.2lf, p-value = %4.3lf, Hypot. = %s  "%(g, p, D < Dcrit) 

        g+=dg

main()
# EOF: main_HGPhaseFunction_verificationTest.py
