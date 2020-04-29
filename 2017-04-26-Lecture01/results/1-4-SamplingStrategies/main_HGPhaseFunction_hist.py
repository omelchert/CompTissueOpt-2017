import sys; sys.path.append('../../src/')
from randomVariateGenerator import * 
from stats import *




def main():

    g = float(sys.argv[1])
    N = int(sys.argv[2])
    myGen = HenyeyGreenstein(g)

    pHG = lambda mu: ((1 - g*g)/(1 + g*g - 2*g*mu)**(3./2))/2
    
    rList = [myGen.generate()[2] for i in range(N)]

    av, sDev, sErr = basicStatistics(rList)
    h = Hist(rList,40)
    #h.dump()

    for i in range(h.nBins-1):
        print h.x(i), h.p(i), h.gErr(i), pHG(h.x(i))
    print "# ", av, sDev, sErr


main()
# EOF: main_HGPhaseFunction_hist.py
