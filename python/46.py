from euler import *
from math import *
from itertools import permutations
from time import time, clock
t = time()

##p = primes(10000)
##oc = []
##for i in range(9,10000,2):
##    if i in p: continue
##    else:
##        oc += [i]
##s = []
##for i in range(1,100):
##    s += [2*(i**2)]
##
##for a in oc:
##    smallest = True
##    for b in p:
##        #print 'oc', a, 'p', b
##        if a-b in s:
##            smallest = False
##            break
##        if b > a:
##            print 'smallest oc is', a
##            break
##    if smallest == True: break

#from sbober
#from tools import primes_upto
from math import sqrt
 
l = 10000
#pset    = set( primes_upto(l) )
pset    = set( primes(l) )
npset   = sorted( list( set(range(9, l, 2)) - pset ) )
sq2set  = set( i*i*2 for i in range(1, int( sqrt(l) )) )
 
for n in npset:
    if not any((n - s) in pset for s in sq2set if s < n):
        print n
        break

print 'time', time()-t

"""
It was proposed by Christian Goldbach that every odd
composite number can be written as the sum of a prime
and twice a square.

9 = 7 + 2x1**2
15 = 7 + 2x2**2
21 = 3 + 2x3**2
25 = 7 + 2x3**2
27 = 19 + 2x2**2
33 = 31 + 2x1**2
It turns out that the conjecture was false.

What is the smallest odd composite that cannot
be written as the sum of a prime and twice a square?
"""
