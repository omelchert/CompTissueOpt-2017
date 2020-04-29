import sys; sys.path.append('../../../src/')
import os
import numpy as np


def jVar(x):
        """compute variance error bars via jacknife resampling

        NOTE: 
        - variance = <x2> - <x>2 
        - error estimates can be computed via two sweeps over
          the data, only! More efficient than bootstrap 
          resampling
        
        Subfcts:
        sDev()          - calls basicStatistics()

        Input:
        x       - data sample

        Returns: (g,gErr)
        var       - variance 
        varErr    - error for variance 
        """
        # compute full sums
        N = x.size 
        xSum = x.sum()
        x2Sum = (x*x).sum() 
        # substract one term to yield jacknifed data sets
        xJack  = (xSum-x)/(x.size-1) 
        x2Jack =  (x2Sum-x*x)/(x.size-1) 

        # compute variance 
        var = x2Sum/N - xSum*xSum/N/N
        # compute error to variance from the 
        # standard deviation of the resampled data sets
        varJack = x2Jack-xJack*xJack   
        varErr = np.sqrt(N-1)*np.std(varJack)
        return var, varErr


def fetchData(fName,col):
    x = []
    with open(fName,'r') as f:
        for line in f:
            c  = line.split()
            if len(c) > col and c[0]!='#':
                x.append(float(c[col]))
    return np.asarray(x)

def main():
    path = sys.argv[1]

    RgData = fetchData(path, 0)
    RData = fetchData(path, 1)
    LData = fetchData(path, 2)
    NData = fetchData(path, 3)

    R = np.sqrt(np.mean(RData*RData))
    Rg = np.sqrt(np.mean(RgData*RgData))
    L = np.mean(LData)
    N = np.mean(NData)

    print "#", path
    print "# (R) (Rg) (L) (N)"
    print R, Rg, L, N 
    

main()
