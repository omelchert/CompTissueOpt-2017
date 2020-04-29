""" main_sampleUnitSphere_BAD.py


Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-19
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from randomVariateGenerator import UnitSphere
from linearCongruentialGenerator import LCG
from math import pi

def main():
    # SIMULATION PARAMETERS
    N = int(sys.argv[1]) 
    seed = 323.
    a, c, m = 106, 1283, 6075 

    # INITIALIZE INSTANCE OF PRNG
    r = LCG(a, c, m, seed/m)

    # INITIALIZE INSTANCE OF UNIT SPHERE SAMPLER
    mySamp = UnitSphere(r.next)

    # SAMPLE RN TRIPLETS 
    for i in range(N):
        x1,x2,x3 = mySamp.generate() 
        print x1,x2,x3

main()
# EOF: main_sampleUnitSphere_BAD.py




