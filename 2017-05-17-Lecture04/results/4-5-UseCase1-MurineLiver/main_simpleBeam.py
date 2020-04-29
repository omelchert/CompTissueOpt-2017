""" main_fluenceRate.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-09
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
import random
from randomVariateGenerator import * 
from photonPacket3D import PhotonPacket 
from irradiationSource import Beam
from volumetricEnergyDensity import EnergyDensity

def notEscaped(x):
    return True if x[2] >= 0.0 else False



def main():
    nP = int(sys.argv[1])          # number of independent photons 
    mua = float(sys.argv[2])       # absorption coefficient
    mus = float(sys.argv[3])       # scattering coefficient
    g = float(sys.argv[4])         # scattering anisotropy

    a0 = 0.15
    rMesh = (0.,0.5,80)
    zMesh = (0.,0.7,100)

    mut = mua + mus                # total attenuation coeff.
    a   = mus/mut                  # single particle albedo
  
    lenSamp = ExpoVariate(mut)     # step length sampler
    dirSamp = HenyeyGreenstein(g)  # directional cosinge sampler
    source = Beam(a0)
    ergDens = EnergyDensity(rMesh, zMesh, nP) 
    
    while(nP):
        random.seed(nP)
        x0 = source.iniPos()
        w0 = source.iniDirCos()
        myPhoton = PhotonPacket(lenSamp.generate, dirSamp.generate, x0=x0, w0=w0)
        while(myPhoton.exists() and notEscaped(myPhoton.x)):
            myPhoton.propagate()
            myPhoton.absorb(a)
            if notEscaped(myPhoton.x):
                ergDens.measure(myPhoton.x, myPhoton.dE)
        nP -= 1
    ergDens.dump()    
        

main()
# EOF: main_fluenceRate.py
