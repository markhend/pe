from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()

##nums = set(int(''.join(i)) for i in (permutations('000000111111222222', 6)))
##skip = set([i*99 for i in range(102)])
##tmp = [909,989,999,1099,1998]
##[skip.add(i) for i in tmp]
skip = [4995,9990]

list=['1','2','10','11','12','20','21','22']
for i in range(1,14): #L[-1] will have 1 more digit than range stop
    for j in list[:len(list)]:
        if len(j) > i:
            list.append(j+'0')
            list.append(j+'1')
            list.append(j+'2')
	
def f(n):
    print n,
    lpm, tmp = 0, 0
    while not lpm:
        tmp += n
        lpm = 1
        if max(str(tmp)) > '2': lpm = 0       
    print tmp
    return tmp

def f(n):
    for i in list:
        tmp = int(i)
        if not tmp % n: return tmp
    print n, "had no f(n) in list"
        
print sum(f(n)/n for n in range(1,9999) if n not in skip)  
#range(1,9999) skip 4995 and 9990 = 314548450056
print 'time', time()-t

"""
For a positive integer n, define f(n) as the
least positive multiple of n that, written in base 10,
uses only digits <= 2.

Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

Also, sum of n:1->100 of f(n)/n = 11363107

Find sum of n:1->10000 of f(n)/n.
"""
