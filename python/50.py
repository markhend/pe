from euler import *
from time import time,clock
from math import *

t=time()
consecutive = 0
answer = 0

p = primes(4000) #adjust so sum(p) is slightly over 10^6

for i in range(len(p)-500):
    j = i + 500 #start with high constant and reduce until answer found
    count = 1
    while sum(p[i:j]) < 1000000:
        #print p[i:j]
        if isprime(sum(p[i:j])):
            if len(p[i:j]) > consecutive:
                consecutive = len(p[i:j])
                answer = sum(p[i:j])
        j += 1

print "consecutive", consecutive, "answer is", answer
print time()-t

##  The prime 41, can be written as the sum of six consecutive primes:
##  41 = 2 + 3 + 5 + 7 + 11 + 13
##  This is the longest sum of consecutive primes that adds
##  to a prime below one-hundred.The longest sum of consecutive
##  primes below one-thousand that adds to a prime, contains
##  21 terms, and is equal to 953. Which prime, below one-million,
##  can be written as the sum of the most consecutive primes?
