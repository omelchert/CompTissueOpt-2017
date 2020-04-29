import numpy as np
from math import cos, acos, sqrt

def dumpLambertProjection(r,nBins):
      """dump Lambert projection

      Write Lambert projection [1] of random variates to standard outstream
      using gnuplots [2] matrix format

      Args:
          r (list of 3-tuples, floats): directional cosine random variates
          nBins (int): number of bins in resulting x and y direction

      Notes:
          full name: Lambert azimuthal equal-area projection (see Ref. [1])
          maps surface of unit sphere to disk of radius 2

      Refs:
          [1] Lambert azimuthal equal-area projection
              https://en.wikipedia.org/wiki/Lambert_azimuthal_equal-area_projection
              [Online; accessed 2017-04-11]

          [2] Gnuplot
              http://www.gnuplot.info
              [Online; accessed 2017-04-11]
      """
      # OBTAIN LAMBERT PROJECTION OF DIRECTIONAL COSINES
      x,y = zip(*map(lambda (x,y,z): 
          (2.*cos(acos(z)/2)*x/sqrt(x*x+y*y), 
          2.*cos(acos(z)/2)*y/sqrt(x*x+y*y)), r))

      # PERFORM 2D BINNING OF RANDOM VARIATES USING NUMPY 
      hist, xBins, yBins = np.histogram2d(
          x, y, nBins, range=[[-2,2],[-2,2]], normed=True)
      
      # DUMP DATA IN GNUPLOT MATRIX FORMAT
      print xBins.size-1,
      for i in range(xBins.size-1):
          print 0.5*(xBins[i] + xBins[i+1] ),
      print

      for i in range(yBins.size-1):
          print 0.5*(yBins[i] + yBins[i+1] ),
          for j in range(xBins.size-1):
              print hist[i,j],
          print
