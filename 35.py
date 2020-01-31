from euler import *
from time import time,clock
from math import *

t = time()
count = 0

for i in range(2,1000001):
    if not isprime(i): continue
    L = list(str(i))
    j,prime_rots = 0,0
    while j<len(L)-1:
        L= L[1:] + L[:1] #rotate
##        print L
        if not isprime(int(''.join(L))):break
        else:
            prime_rots+=1
##            print i, num_prime_rots, len(L)-1
        j+=1
    if prime_rots==len(L)-1:
        count+=1

print "answer is", count

print time()-t

##The number, 197, is called a circular prime because
##all rotations of the digits: 197, 971, and 719, are themselves prime.
##
##There are thirteen such primes below 100:
##2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
##
##How many circular primes are there below one million?

##code snippets:
##factorials = {'0' : 1, '1' : 1, '2' : 2, '3' : 6, '4' : 24, '5' : 120,
##              '6' : 720, '7' : 5040, '8' : 40320, '9' : 362880}
##return sum(num for num in xrange(3, 50000) if num == sum(factorials[x] for x in str(num)))

##def rotate(L, N):
##       return L[N:] + L[:N]
