import sys; sys.path.append('../../src/')
from randomVariateGenerator import * 
from stats import *

def check(g,(av,sErr)):
    if abs(g-av) <= 2*sErr:
       myStr = "passed"
    else:
       myStr = "not passed"
    return myStr


def main():

    # DECLARE AND INITIALIZE SIMULATION PARAMETERS 
    N = int(sys.argv[1])
    g, dg = 0.0, 0.1

    print "# (g) (av) +/ (sErr) : (status)"
    while g < 1.0:
        myGen = HenyeyGreenstein(g)
        rList = [myGen.generate()[2] for i in range(N)]
        av, sDev, sErr = basicStatistics(rList)
        print "%3.2lf  %5.4lf +- %5.4lf  :  %s "%\
            (g, av, sErr, check(g,(av,sErr)))
        g += dg

main()
# EOF: main_HGPhaseFunction_verificationTest.py
