""" pmf.py

module implementing data structure to handle probabiltiy mass functions 

Supplementary material for the lecture "Computational Photonics" held at 
Leibniz University Hannover in summer term 2017

DATE: 2017-04-27
AUTHOR: O. Melchert
"""

class PMF(object):
     def __init__(self):
         self.pmf = {}
         self.n = 0
     
     def add(self,k):
         self.pmf[k] = self.pmf.get(k,0) + 1
         self.n += 1

     def dump(self):
         print "# (x) (f(x)) (p(x))"
         for (k,v) in sorted(self.pmf.items()):
             print k, v, float(v)/self.n

# EOF: pmf.py
