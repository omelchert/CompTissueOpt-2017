""" linearCongruentialGenerator.py

Module illustrating the implementation of a linear congruential generator

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017
"""

def LCG(a,c,m,x0):
    """ linear congruential generator

    Implements linear congruential generator following Ref. [1]

    Args: 
        a (int): multiplier
        c (int): increment
        m (int): modulus
        x0 (float): starging value in range [0,1)
    
    Returns:
        nothing, used as generator

    Notes:
        The starting value in Ref. [1] is taken as a positive integer and the 
        resulting sequence of random numbers is divided by the modulus m in 
        order to obain numbers in the interval [0,1). In contrast, the given 
        implementation expects a starting value from the range [0,1) and 
        returns already scaled samples.

        Subsequent pseudo random samples can be obtained by calling the next()
        method of the generator.

    Refs:
        [1] Random Number Generators
            Hull, T.E. and Dobell, A.R.
            SIAM Review, 4 (1962) 230
    """ 
    x = x0*m
    while 1:
        x = (a*x + c)%(m)
        yield float(x)/m

# EOF: linearCongruentialGenerator.py
