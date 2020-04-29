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
from irradiationSource import Fiber 
from volumetricEnergyDensity import EnergyDensity


def main():
    nP = int(sys.argv[1])          # number of independent photons 
    mua = float(sys.argv[2])       # absorption coefficient
    mus = float(sys.argv[3])       # scattering coefficient
    g = float(sys.argv[4])         # scattering anisotropy

    a0 = 0.15                      # beam radius
    NA = 0.4                       # numerical apperture of fiber
    nf = 1.45                      # refractive index of fiber
    nm = 1.33                      # refractive index ot tissue (mostly water)

    rM = (0.,0.5,80)               # measurement domain - radial mesh 
    zM = (0.,0.7,100)              # measurement domain - z-mesh 

    mut = mua + mus                # total attenuation coeff.
    a   = mus/mut                  # single particle albedo
  
    lenSamp = ExpoVariate(mut)     # step length sampler
    dirSamp = HenyeyGreenstein(g)  # directional cosinge sampler
    source = Fiber(a0,NA,nf,nm)    # irradiation source 
    Wrz = EnergyDensity(rM,zM,nP)  # measurement - observable

    # SET Z=0 AS TISSUE SURFACE
    notEscaped = lambda z: True if z >= 0. else False

    while(nP):
        random.seed(nP)
        myPhoton = PhotonPacket(lenSamp.generate, dirSamp.generate, x0=source.iniPos(), w0=source.iniDirCos())
        while(myPhoton.exists() and notEscaped(myPhoton.x[2])):
            myPhoton.propagate()
            myPhoton.absorb(a)
            Wrz.measure(myPhoton.x, myPhoton.dE)
        nP -= 1

    (z,Wz) = Wrz.Wz()
    for i in range(z.size):
        print z[i], Wz[i]/mua


    #Wrz.dump()    
        

main()
# EOF: main_fluenceRate.py
