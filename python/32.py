from euler import *
from time import time,clock
from math import *
from itertools import permutations

t = time()
sum_set = set()
digits='123456789'

multiplicand = list(permutations(digits,3))
multiplier = list(permutations(digits,2))

for i in multiplicand:
    a = ''.join(i)
    for j in multiplier:
        if set(j)-set(i) <> set(j):continue
        b = ''.join(j)
        c = int(a) * int(b)
        checkset = set(digits) - set(i) - set(j)
        if sorted(list(str(c))) == sorted(list(checkset)):
            sum_set.add(c)

print "sum_set is", sum_set     
print "answer is", sum(sum_set)
print time()-t

##We shall say that an n-digit number is pandigital
##if it makes use of all the digits 1 to n exactly once;
##for example, the 5-digit number, 15234, is 1 through 5 pandigital.
##
##The product 7254 is unusual, as the identity,
##39  186 = 7254, containing multiplicand, multiplier,
##and product is 1 through 9 pandigital.
##
##Find the sum of all products whose
##multiplicand/multiplier/product identity
##can be written as a 1 through 9 pandigital.
##
##HINT: Some products can be obtained in
##more than one way so be sure to only include it once in your sum.

##code snippets:
##factorials = {'0' : 1, '1' : 1, '2' : 2, '3' : 6, '4' : 24, '5' : 120,
##              '6' : 720, '7' : 5040, '8' : 40320, '9' : 362880}
##return sum(num for num in xrange(3, 50000) if num == sum(factorials[x] for x in str(num)))

##def rotate(L, N):
##       return L[N:] + L[:N]
