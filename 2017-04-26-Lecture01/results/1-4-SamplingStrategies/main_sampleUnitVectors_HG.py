""" main_sampleUnitVectors.py


Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-19
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from randomVariateGenerator import HenyeyGreenstein 

def main():
    # SIMULATION PARAMETERS
    g = float(sys.argv[1])
    N = int(sys.argv[2]) 


    # INITIALIZE INSTANCE OF UNIT SPHERE SAMPLER
    mySamp = HenyeyGreenstein(g)

    # SAMPLE RN TRIPLETS 
    for i in range(N):
        x1,x2,x3 = mySamp.generate() 
        print x1,x2,x3

main()
# EOF: main_sampleUnitVectors.py
