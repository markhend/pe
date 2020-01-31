from euler import *
#from math import 
#from itertools import permutations
from time import time,clock
t = time()
answer = 0

###print str(28433*2**7830457+1)[-10:]
##print str(2**7830457+1)[-10:]
###then result of the above less 1 * 28433, plus one
###answer is 8739992577

##a = 2**7830457
##b = a% 10000000000 # last 10 digits of 2**(...)
###b = int( a% 10000000000 ) # last 10 digits of 2**(...)
##c = b * 28433
##c = c+1
##print c % 10000000000   # last 10 digits

print str( pow( 2, 7830457, 10 ** 10 ) * 28433 + 1 )[-10:]

#sbober
#print (28433 * pow(2, 7830457, 10**10) + 1) % 10**10
    
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
