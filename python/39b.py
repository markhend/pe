from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0
p=[]

for i in permutations(range(1,401),3):
    a = i[0]
    b = i[1]
    c = i[2]
    if c < a or c < b: continue
    if a+b+c > 1000: continue
    if a**2 + b**2 == c**2:
        p.append(a+b+c)
##    print i
d = {}
for i in range(1,1001):
	d[i] = 0
for i in p:
    d[i]+=1
m = max(d, key=d.get)
print m

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
##
##m = max(d, key=d.get)
