""" main_RANDU.py

Script implementing spectral test the particular Park-Miller type linear
congruential pseudo-random number generator (PRNG) RANDU. It was used as the
standard PRNG on IBM machines during the 1960s. 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-11
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from linearCongruentialGenerator import LCG

def main():
    # PARAMETER SETTING DEFINING RANDU GENERATOR
    a = 65539   
    c = 0
    m = 2**31
    s = 323.

    # INITIALIZE INSTANCE OF PRNG
    r = LCG(a, c, m, s/m)

    # SAMPLE RN TRIPLETS 
    r1, r2, r3 = r.next(), r.next(), r.next()
    for i in range(10000):
        print r1, r2, r3
        r1, r2, r3 = r2, r3, r.next()

main()
# EOF: main_RANDU.py
