""" rngSwitch.py

module implementing data structure that allows to choose from a set of PRNGs 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""
import random
from linearCongruentialGenerator import LCG


def fetchPRNG(mode=None, seed = 323):
    """pseudo random number generator (PRNG) handler

    Hack emulating switch statement of other languages for easy change of PRNG

    Args:
        mode (str) PRNG type (choices: BAD, MIN, RANDU; default: MT)
        seed (int) integer seed for prng

    Returns:
        r (object) random number generator
    """
    random.seed(seed)
    return {
        'BAD': LCG(106, 1283, 6075, float(seed)/6075 ).next,               
        'MIN': LCG(16807, 0, 2147483647, float(seed)/2147483647).next,
        'RANDU': LCG(65539, 0, 2147483648, float(seed)/2147483648).next,
    }.get(mode, random.random)


# EOF: rngSwitch.py
