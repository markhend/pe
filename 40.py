from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0

d='0'
for i in range(1,1000001):
    d+=str(i)
print int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])

print 'time', time()-t

##An irrational decimal fraction is created by
##concatenating the positive integers:
##0.123456789101112131415161718192021...
##
##It can be seen that the 12th digit of the
##fractional part is 1.
##If dn represents the nth digit of the fractional part,
##find the value of the following expression.
##
##d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

##def rotate(L, N):
##       return L[N:] + L[:N]
##
##m = max(d, key=d.get)
