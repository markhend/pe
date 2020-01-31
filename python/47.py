from euler import *
from time import time,clock

t=time()

primes = primes(200000)
consec = 0
factors = [None]*200000
factors[2] = 2


for n in xrange(4,200000):
   x = n
   if x in primes:
      consec = 0
      continue
   l = []
   used_lookup = False
   while x not in primes:
      if factors[x] is not None:
         #print "used lookup"
         l = l+factors[x]
         used_lookup = True
         break
      for i in primes:
         if i > x/2: break
         if x%i == 0:
             x = x/i
             l.append(i)
             break
   if not used_lookup:
      l.append(x)
   factors[n] = l
   #print n, l
   if len(set(l)) == 4: consec += 1
   else: consec = 0
   if consec == 4:
      print n-3, n-2, n-1, n
      break

print time()-t

##    The first two consecutive numbers to have two
##    distinct prime factors are:
##    14 = 2 x 7
##    15 = 3 x 5
##    The first three consecutive numbers to have three
##    distinct prime factors are:
##    644 = 2^2 x 7 x 23
##    645 = 3 x 5 x 43
##    646 = 2 x 17 x 19.
##    Find the first four consecutive integers to have four
##    distinct prime factors. What is the first of these numbers?
