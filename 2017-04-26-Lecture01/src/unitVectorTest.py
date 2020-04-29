""" unitVectorTest.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-25
AUTHOR: O. Melchert
"""
import scipy.stats
from stats import Hist, basicStatistics 
from math import sqrt, exp, pi


class RandomnessTest(object):
    """ Class implementing randomness test for unit vectors

    Implements Stephens approximate test to check for randomness of unit 
    vectors detailed in section 4.2 of Ref. [1]. 

    Refs:
        [1] The testing of unit vectors for randomness
            Stephens, M. A.,
            J. Amer. Statist. Assoc., 59 (1964) 160 
    """
    def __init__(self, sampler, N, M):
        """initializes instance of randomness test

        Args:
            sampler (object) unit sphere sampler
            N (int) sample size
            M (int) number of samples

        Attrib:
            name (str) name of the class object that implements sampler object
            res (array) sample of resultant vectors 
        """
        self.sampler = sampler
        self.name = sampler.__class__.__name__
        self.N = N
        self.M = M
        self.res = [self._resultantVectorLength(N) for m in range(M)]

    def _getSingleSample(self, N):
        """generate sample of unit vectors
        
        Args:
            N (int) sample size

        Returns:
            samp (list of 3-tuples) sample comprising N unit vectors
        """
        return [self.sampler.generate() for n in range(N)]

    def _resultantVectorLength(self,N):
        """length of resultant vector

        Computes length of resultant vector obtained by summing up N unit
        vectors

        Args:
            N (int) sample size

        Returns:
            R (float) length of resultant vector 
        """
        x, y, z = zip(*self._getSingleSample(N))
        X, Y, Z = sum(x), sum(y), sum(z)
        return sqrt(X*X + Y*Y + Z*Z) 

    def R(self):
        """resultant vector summary statistics
        
        Computes mean and standard deviation of the sampled resultant vectors

        Notes:
            - uses basicStatistics method defined in stats.py
        """
        av, sDev, sErr = basicStatistics(self.res)
        return av, sErr
    
    def pdf(self, nBins=20):
        """probability density function of resultant vectors
        
        Plots probability density function of the sampled resultant vectors

        Args:
            nBins (int) number of bins for creating pdf 

        Notes:
            - uses histogram class defined in stats.py
        """
        # RAYLEIGH LIMITING FORM - REF. [1], EQ. (4) 
        fR = lambda x: 3.*sqrt(6)*x*x*exp(-3.*x*x/2/self.N)/sqrt(pi)/sqrt(self.N**3)

        hist = Hist(self.res, nBins) 
        print "# PDF FOR SAMPLED RESULTANT VECTORS:"
        print "# (R) (p(R)) (err) (fRay(R))"
        for i in range(hist.nBins-1):
            print hist.x(i), hist.p(i), hist.gErr(i), fR(hist.x(i))

        print "# SUMMARY STATISTICS:"
        # STATISTICS OF RESULTANT VECTOR
        av, sErr = self.R()
        print "# av(R) +- sErr(R) = %lf +- %lf "%( av, sErr)
        print


    def checkRandomness(self, a=0.05):
        """approximate randomness test

        Implements Stephens approximate test to check for randomness of unit 
        vectors detailed in section 4.2 of Ref. [1]. 

        Args:
            a (float) confidence level (in range 0...1) 

        Notes:
            - asymptotically correct test
            - good agreemnt already for a = 0.05 and N > 10
            - test is based on the asymptotic statistics of the resultant 
              vector of N independent unit vectors
            - TEST OUTLINE: 
              
              Null hypothesis: 
                  The null hypothesis is that the N given vectors are from a 
                  population uniformly distributed in 3 dimensions.

              Aproximate test:
                  (1) find R, i.e. the length of the resultant vector
                  (2) find R0 =  sqrt( chi2(a=0.05, dof=3)*N/3 ), where chi2 is 
                      the distribution of the sum of squares of 3 independent 
                      standard normal random variables
                  (3) if R > R0 reject the hypothesis at confidence level a

        Refs:
            [1] The testing of unit vectors for randomness
                Stephens, M. A.,
                J. Amer. Statist. Assoc., 59 (1964) 160 
        """
        # APPROXIMATE TEST STATISTICS FOR COFIDENCE LEVEL a (a-SIGNIFICANCE)
        R0 = sqrt(scipy.stats.chi2.isf(a, 3)*float(self.N)/3)
        # STATISTICS OF RESULTANT VECTOR
        av, sErr = self.R()

        print "# TETS NULL HYPOTHESIS FOR SAMPLER: %s"%(self.name)
        print "# av(R) +- sErr(R) = %lf +- %lf "%( av, sErr)
        print "# R0 = %lf"%(R0)
        print "# REJECT NULL HYPOTHESIS (SIGNIFICANCE LEVEL %3.2lf): %s "%(a, av>R0)
        print "# TEST RESULT: %s"%("OK" if av<=R0 else "FAILED")


# EOF: unitVectorTest.py
