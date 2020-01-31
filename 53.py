from euler import *
from math import *
#from itertools import permutations
from time import time,clock
t = time()
count = 0
##
##f = factorial
##for n in range(100,0,-1):
##   for r in range(n+1):
##      if f(n)/(f(r)*f(n-r)) > 10**6: count += 1
##print count

fac = {0: 1}
for i in range(1, 101):
    fac[i] = reduce(lambda x, y: x * y, range(1, i + 1))
 
def c(n, r):
##   return fac.get(n) / (fac.get(r) * fac.get(n - r))
   return fac[n] / (fac[r] * fac[n-r])

nums = []
for n in range(1, 101):
    for r in range(1, n + 1):
        nums.append(c(n, r))
 
print len(filter(lambda x: x > 1000000, nums))

print 'time', time()-t


"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,
nCr =	n!/r!(n-r)!,where r <= n, n! = nx(n1)x...x3x2x1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr,
for 1 <= n <= 100, are greater than one-million?
"""
