from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0

for p in range(800,1001):
    count=0
    for a in range(1,p):
        for b in range(1,p):
            c = p-a-b
            if a**2 + b**2 == c**2:
                count+=1
    if count: print p, count

            
print 'time', time()-t

##If p is the perimeter of a right angle triangle
##with integral length sides, {a,b,c}, there are
##exactly three solutions for p = 120.
##
##{20,48,52}, {24,45,51}, {30,40,50}
##
##For which value of p <= 1000, is the number of solutions maximised?

##def rotate(L, N):
##       return L[N:] + L[:N]
