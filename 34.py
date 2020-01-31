from euler import *
from time import time,clock
from math import *

t=time()
answer = 0

for i in xrange(3,100000):
    if i == sum(factorial(int(j)) for j in str(i)):
        print i
        answer += i

print "answer is", answer

print time()-t

##shorter example:
##factorials = {'0' : 1, '1' : 1, '2' : 2, '3' : 6, '4' : 24, '5' : 120,
##              '6' : 720, '7' : 5040, '8' : 40320, '9' : 362880}
##return sum(num for num in xrange(3, 50000) if num == sum(factorials[x] for x in str(num)))
##
##145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##
##Find the sum of all numbers which are equal to the sum
##of the factorial of their digits.
##
##Note: as 1! = 1 and 2! = 2 are not sums they are not included.
