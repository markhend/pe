from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0

for i in [str(x) for x in xrange(9,1000000) if isprime(x)]:
    prime = True
    for j in range(len(i)):
        a = i[j:]
        if j==0: b=a
        else: b = i[:-j]
##        print a,b
        if a.startswith('0') or b.startswith('0'):
            prime = False
            break
        if not (isprime(int(a)) and isprime(int(b))):
            prime = False
            break
    if prime == True:
        answer += int(i)
        print i, 'is one of eleven'
        
print "answer is", answer
print time()-t

##The number 3797 has an interesting property.
##Being prime itself, it is possible to continuously
##remove digits from left to right, and remain prime
##at each stage: 3797, 797, 97, and 7.
##Similarly we can work from right to left:
##    3797, 379, 37, and 3.
##Find the sum of the only eleven primes that are
##both truncatable from left to right and right to left.
##NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

##def rotate(L, N):
##       return L[N:] + L[:N]
