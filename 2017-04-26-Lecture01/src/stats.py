import sys
import numpy as np
from math import sqrt, floor, log, exp

def mean(myList):
        return float(sum(myList))/len(myList)

def basicStatistics(myList):
	"""compute mean value, standard deviation,
	and standard error of the mean for the 
	supplied list of numerical values

	NOTE: so as to reduce roundoff errors, 
	variance is computed via the corrected
	two-pass algorithm

	Input:
	myList	-- sequence of numerical values

	Returns: (av,sDev,sErr)
	av	-- mean value
	sDev	-- standard deviation
	sErr	-- standard error of the mean
	"""
	av=var=tiny=0.
	N  = len(myList) 
        av = mean(myList)
	for el in myList:
		dum   = el - av
		tiny += dum
		var  += dum*dum
	var = (var - tiny*tiny/N)/(N-1)
	sDev = sqrt(var)
	sErr = sDev/sqrt(N)
	return av, sDev, sErr


class Hist(object):

    def __init__(self, a, nBins, r = None):
        self.nBins = nBins
        (self.hist, self.bins) = np.histogram(a,nBins,range=r)
        self.N = np.sum(self.hist) 

    def _hRel(self,i):
        return float(self.hist[i])/self.N

    def _w(self,i):
        return self.bins[i+1] - self.bins[i]

    def x(self,i):
        return 0.5*(self.bins[i]+self.bins[i+1])

    def p(self,i):
        return self._hRel(i)/self._w(i)

    def freq(self,i):
        return self.hist[i]

    def gErr(self,i):
        return np.sqrt(self._hRel(i)*(1.-self._hRel(i))/(self.N-1))/self._w(i)

    def dump(self):
        for i in range(self.nBins-1):
            print self.x(i), self.p(i), self.gErr(i)

