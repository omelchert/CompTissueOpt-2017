""" main_photonPropagation_S.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-09
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
import random
from randomVariateGenerator import * 
from photonPacket3D import PhotonPacket 


def main():
    N = int(sys.argv[1])           # number of steps to take
    g = float(sys.argv[2])         # scattering anisotropy

    mua = 2.0                      # absorption coefficient
    mus = 20.0                     # scattering coefficient
    mut = mua + mus                # total attenuation coeff.
    a   = mus/mut                  # single particle albedo
  
    random.seed(0)
    lenSamp = ExpoVariate(mut)     # step length sampler 
    dirSamp = HenyeyGreenstein(g)  # direction sampler

                                   # photon packet random walker
    myPhoton = PhotonPacket(lenSamp.generate,dirSamp.generate)
    
    for i in range(N):
        myPhoton.propagate()
        print myPhoton

main()
# EOF: main_photonPropagation_S.py
