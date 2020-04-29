""" main_fluenceRate.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-09
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
import random
from randomVariateGenerator import * 
from fluenceRate import FluenceRate
from photonPacket3D import PhotonPacket 


def main():
    nP = int(sys.argv[1])          # number of independent photons 
    mua = float(sys.argv[2])       # absorption coefficient
    mus = float(sys.argv[3])       # scattering coefficient
    g = float(sys.argv[4])         # scattering anisotropy
    nBins = 100                    # number of bins for measurement

    mut = mua + mus                # total attenuation coeff.
    a   = mus/mut                  # single particle albedo
  
    lenSamp = ExpoVariate(mut)     # step length sampler
    dirSamp = HenyeyGreenstein(g)  # directional cosinge sampler
    Phi = FluenceRate(nBins,nP)    # fluence rate data structure
    
    while(nP):
        random.seed(nP)
        myPhoton = PhotonPacket(lenSamp.generate, dirSamp.generate)
        while(myPhoton.exists()):
            myPhoton.propagate()
            myPhoton.absorb(a)
            Phi.measure(myPhoton.x, myPhoton.dE)
        nP -= 1

    Phi.dump()
        

main()
# EOF: main_fluenceRate.py
