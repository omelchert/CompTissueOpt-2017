""" main_minimalStandard.py

Script implementing spectral test for the particular Park-Miller type prime
modulus multiplicative linear congruential generator (PMMLCG), short 'Lehmer'
generator, referred to as the 'minimal standard' [1,2]. 

Refs:
    [1] Random number generators: Good ones are hard to find
        Park, S.K. and Miller, K.W.
        Communications of the ACM, 31 (1988) 1192

    [2] Numerical Recipes in Fortran 77
        Press, WH and Teukolsky, SA and Vetterling, WT and Flannery, BP
        Cambridge University Press (2nd Edition, 2002)

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017
        
DATE: 2017-04-11
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from linearCongruentialGenerator import LCG

def main():
    # PARAMETER SETTING DEFINING MINIMAL STANDARD 
    a = 16807
    c = 0
    m = 2147483647
    s = 323.

    # INITIALIZE INSTANCE OF PRNG
    r = LCG(a, c, m, s/m)

    # SAMPLE RN TRIPLETS 
    r1, r2, r3 = r.next(), r.next(), r.next()
    for i in range(10000):
        print r1, r2, r3
        r1, r2, r3 = r2, r3, r.next()

main()
# EOF: main_minimalStandard.py
