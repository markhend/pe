from euler import *
from time import time,clock
from math import *

t=time()

p = primes(3956) #adjust so sum(p) is slightly over 10^6

length = len(p)
done = False
while(not done):
    i = 0
    j = length
    while sum(p[i:j]) < 10**6:
        print i, j
        if isprime(sum(p[i:j])):
            print "slice "+"["+str(i)+":"+str(j)+"]", "length", len(p[i:j])
            print "answer", sum(p[i:j])
            done = True
        i,j = i+1,j+1
    length -= 1

print time()-t

##  The prime 41, can be written as the sum of six consecutive primes:
##  41 = 2 + 3 + 5 + 7 + 11 + 13
##  This is the longest sum of consecutive primes that adds
##  to a prime below one-hundred.The longest sum of consecutive
##  primes below one-thousand that adds to a prime, contains
##  21 terms, and is equal to 953. Which prime, below one-million,
##  can be written as the sum of the most consecutive primes?
