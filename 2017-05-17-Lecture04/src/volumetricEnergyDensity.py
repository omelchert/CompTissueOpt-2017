""" volumetricEnergyDensity.py

module implementing volumetric energy density 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-16
AUTHOR: O. Melchert
"""
import numpy as np

class EnergyDensity(object):
    """class defining data structure for measurement of absorbed energy 
    """
    def __init__(self,(rMin,rMax,Nr), (zMin,zMax,Nz), nP):
        """initialize an instance of energy density data structure

        Args:
            rMin (float) lowest r-sample
            rMax (float) largest r-sample
            Nr (int) number of r meshpoints
            zMin (float) lowest z-sample
            zMax (float) largest z-sample
            Nz (int) number of z meshpoints
            nP (int) number of photons for normalization

        Attrib:
            shellWidth (float) shell width in microns (default: 50 mu)
            h (array) bins for energy accumulation
            Nr (int) number of r meshpoints
            Nz (int) number of z meshpoints
            r (numpy-array) r-mesh
            dr (float) r increment
            z (numpy-array) z-mesh
            dz (float) z increment
            W (numpy-array, ndim=2) data storage
        """
        self.nP = nP
        self.Nr = Nr
        self.Nz = Nz
        self.r, self.dr = np.linspace(rMin,rMax,Nr,endpoint=False, retstep=True)
        self.z, self.dz = np.linspace(zMin,zMax,Nz,endpoint=False, retstep=True)
        self.W = np.zeros((Nr+1,Nz+1),dtype=float)
            
    def pos2bin(self,pos):
        """convert packet position to bin id

        Args:
            pos (3-tuple) position in 3d space

        Returns: (ri,zi) 
            ri (int) integer identifier for r-location
            zi (int) integer identifier for z-location
        """
        x, y, z = pos
        ri = int(np.sqrt(x*x + y*y)/self.dr) 
        zi = int(z/self.dz) if int(z/self.dz) >= 0 else self.Nz    
        return min(self.Nr, ri), min(self.Nz, zi)

    def measure(self,pos,dE):
        """accumulate absorbed photon weight in corresponding bin
        """
        ir, iz = self.pos2bin(pos)  
        self.W[ir,iz] += dE

    def Wz(self):
        """internal fluence

        Note:
            - uses the fact that array self.W is not normalized

        Returns:
            z (numpy-array) offset z-mesh containing reference positions 
            Wz (numpy-array) internal fluence
        """
        Wz = np.asarray([np.sum(self.W[:-1,j]) for j in range(self.Nz)])/self.dz/self.nP
        z = self.z+self.dz/2
        return z,Wz


    def dump(self):
        """list absorbed energy density 

        dumps absorbed energy densitiy to standard output. Data format is 
        gnuplots nonuniform matrix 

        Note:
            - can be plotted with via command 
                p 'data.out' nonuniform matrix with image

        """
        fac = 2*np.pi*self.dr*self.dr*self.dz 
        WNorm = self.W[:,:]/self.nP/fac
        print self.r.size,
        for r in self.r:
            print r,
        print
        Wsum = 0.
        for zi,z in enumerate(self.z):
            print z,
            for ri in range(self.r.size):
                w = WNorm[ri,zi]/(ri+0.5)
                print w,
            print

# EOF: volumetricEnergyDensity.py 
