from euler import *
from math import *
#from itertools import permutations
from time import time,clock
t = time()
answer = 0

##for a in range(2,100):
##    for b in range(2,100):
##        sum_digits = sum(int(c) for c in str(a**b))
##        if sum_digits > answer: answer = sum_digits
##print answer

print max(sum(map(int, str(a**b))) for a in range(1,100) for b in range(1,100))

print 'time', time()-t


"""
A googol (10**100) is a massive number: one followed by
one-hundred zeros; 100**100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size,
he sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b,
where a, b < 100, what is the maximum digital sum?
"""
