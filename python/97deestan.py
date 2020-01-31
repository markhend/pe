from euler import *
from math import *
#from itertools import permutations
from time import time,clock
t = time()

answer = 1
for i in xrange(7830457/20):
    answer = (answer * 2**20) % 10**10
for i in xrange(7830457%20):
    answer = (answer * 2) % 10**10
answer = (answer * 28433 + 1) % 10**10
 
print answer
    
print 'time', time()-t


"""
The first known prime found to exceed one million digits
was discovered in 1999, and is a Mersenne prime of the form
2**6972593-1; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2**p-1,
have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne
prime which contains 2,357,207 digits: 28433x2**7830457+1.

Find the last ten digits of this prime number.
"""
