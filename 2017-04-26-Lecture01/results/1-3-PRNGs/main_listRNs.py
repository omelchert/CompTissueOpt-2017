""" main_listRNs.py

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-11
AUTHOR: O. Melchert
"""
import sys; sys.path.append('../../src/')
from linearCongruentialGenerator import LCG

def main():
    # PARAMETER SETTING DEFINING RANDU GENERATOR
    N = int(sys.argv[1])
    s = float(sys.argv[2])
    a = 16807
    c = 0
    m = 2147483647

    # INITIALIZE INSTANCE OF PRNG
    r = LCG(a, c, m, s)

    # SAMPLE RNs
    for i in range(N):
        print r.next()

main()
# EOF: main_listRNs.py
