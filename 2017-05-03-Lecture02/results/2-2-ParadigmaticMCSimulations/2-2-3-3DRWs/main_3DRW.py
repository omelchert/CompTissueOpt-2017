""" main_3DRW.py

script for Monte Carlo sampling of 3D random walk

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-05-02
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../../src/')
from randomVariateGenerator import * 
from randomWalker3D import RandomWalker3D 

def main():
    N = int(sys.argv[1]) 
    g = float(sys.argv[2])
    mySamp = HenyeyGreenstein(g)
    myRW = RandomWalker3D(mySamp.generate)

    for i in range(N):
        x,y,z = myRW.x
        print myRW.nSteps, x, y, z 
        myRW.step()

main()
# EOF: main_3DRW.py
