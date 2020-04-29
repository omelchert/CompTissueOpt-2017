""" main_3DRW_iso.py

script for Monte Carlo sampling of 1D random walk endpositions

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
from randomWalker3D_iso import RandomWalker3D_iso

def main():
    N = int(sys.argv[1]) 
    myRW = RandomWalker3D_iso()

    for i in range(N):
        x,y,z = myRW.x
        print myRW.nSteps, x, y, z 
        myRW.step()

main()
# EOF: main_3DRW_iso.py
