import sys; sys.path.append('../../../src/')
import numpy as np
from randomVariateGenerator import * 
from randomWalker3D import RandomWalker3D 
from stats import *

def resultant(m,g,N):
    np.random.seed(m)
    mySamp = HenyeyGreenstein(g,np.random.random)
    myRW = RandomWalker3D(mySamp.generate)
    for i in range(N):
        myRW.step()
    x,y,z = myRW.x
    return np.sqrt(x*x+y*y+z*z)


def main():
    N = int(sys.argv[1]) 
    M = int(sys.argv[2])
    g = float(sys.argv[3])

    RList = [resultant(m,g,N) for m in np.random.randint(sys.maxint, size=M)]

    av, sDev, sErr = basicStatistics(RList)
    print "# SUMMARY STATISTICS FOR SETUP:"
    print "#", sys.argv[1:]
    print "# (N) (av) (err)"
    print N, av, sErr

main()
