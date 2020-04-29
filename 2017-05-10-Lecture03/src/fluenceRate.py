from math import sqrt, log, pi

class FluenceRate(object):
    """class defining data structure for measurement of fluence rate
    """
    def __init__(self,nBins,nP):
        """initialize an instance of fluence rate data structure

        Args:
            nBins (int) number of bins for data accumulation
            nP (int) number of photons for normalization

        Attrib:
            shellWidth (float) shell width in microns (default: 50 mu)
            h (array) bins for energy accumulation
        """
        self.nBins      = nBins 
        self.nPhotons   = nP
        self.shellWidth = 50
        self.h          = [0. for i in range(nBins)] 
            
    def pos2bin(self,pos):
        """convert packet position to bin id
        """
        x,y,z   = pos
        r       = sqrt(x*x+y*y+z*z)
        myBin   = int(r/self.shellWidth/1e-4)
        if myBin >= self.nBins-1:
                  myBin = self.nBins-1
        return myBin

    def measure(self,x,dE):
        """accumulate absorbed photon weight in corresponding bin
        """
        self.h[self.pos2bin(x)]+=dE

    def dump(self):
        """list fluence rate
        """
        print "# (r)  (h(r))"
        fac = 4*pi*pow(self.shellWidth,3)*self.nPhotons*1e-12
        for i in range(self.nBins-1):
                print i*self.shellWidth*1e-4, self.h[i]/(fac*(i*i+i+1./3.))


