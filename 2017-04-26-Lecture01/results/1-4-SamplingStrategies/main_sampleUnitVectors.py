""" main_sampleUnitVectors.py


Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-19
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from randomVariateGenerator import UnitSphere

def main():
    # SIMULATION PARAMETERS
    N = int(sys.argv[1]) 

    # INITIALIZE INSTANCE OF UNIT SPHERE SAMPLER
    mySamp = UnitSphere()

    # SAMPLE RN TRIPLETS 
    for i in range(N):
        x1,x2,x3 = mySamp.generate() 
        print x1,x2,x3

main()
# EOF: main_sampleUnitVectors.py
