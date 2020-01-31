from euler import *
from math import *
#from itertools import permutations
from time import time,clock
t = time()
answer = 0

##for n in range(1000012,1000020):
##   Rk = 1
##   if gcd(n, 10) == 1:
##      while True:
##         Rk = Rk*10 + 1
##         if Rk % n == 0:
####            print 'n is', n, 'A(n) is', len(str(Rk))
##            break
##   if len(str(Rk)) > 333336:
##      print 'n is', n, 'A(n) is', len(str(Rk))
##      break

for n in range(1000012,10000000):
   Rk = 1
   if gcd(n, 10) == 1:
      while True:
         Rk = Rk*10 + 1
         if Rk % n == 0:
##            print 'n is', n, 'A(n) is', len(str(Rk))
            break
   if len(str(Rk)) > 1000000:
      print 'n is', n, 'A(n) is', len(str(Rk))
      break


print 'time', time()-t


"""
A number consisting entirely of ones is called a repunit.
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1,
it can be shown that there always exists a value, k,
for which R(k) is divisible by n, and let A(n) be the
least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""
