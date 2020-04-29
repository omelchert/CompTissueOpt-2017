import sys; sys.path.append('../../src/')
import numpy as np
from steadyStateFluence import *

def main():
        mua  = 1.0
        mus  = 1.0
        g    = float(sys.argv[1])
        N    = 20

        x,dx = np.linspace(0.001,20,2000,retstep=True)
        k,dk = np.linspace(-np.pi/dx,np.pi/dx,2000,retstep=True)

        LM0FDR = LM0ReprFreqDom((mua,mus,g),N,k)
        LM0 = LM0Repr(LM0FDR,x,dk)

        phi0r = fluence(x,LM0)

        for i in range(len(phi0r)):
            print x[i], phi0r[i]

main()
