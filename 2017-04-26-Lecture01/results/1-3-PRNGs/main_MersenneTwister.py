""" main_minimalStandard.py

Script implementing spectral test for the Mersenne Twister PRNG implemented 
by Python's random module

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017
        
DATE: 2017-04-11
AUTHOR: O. Melchert
"""
import random

def main():
    random.seed(0)
    r = random.random

    r1, r2, r3 = r(), r(), r()
    for i in range(10000):
        print r1, r2, r3
        r1, r2, r3 = r2, r3, r()

main()
# EOF: main_MersenneTwister.py
