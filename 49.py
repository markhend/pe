from euler import *
from time import time,clock

t=time()

p = [n for n in primes(10000) if n > 999]

def solve():
    res = ((a,b,c,) for a in p
           for b in p
           if b > a
           for c in p
           if c > b
           if c-b == b-a
           if sorted(str(a)) == sorted(str(b)) == sorted(str(c))
    )
    print next(res)
    print next(res)

solve()

print time()-t


##    The arithmetic sequence, 1487, 4817, 8147, in which each of the
##    terms increases by 3330, is unusual in two ways: (i) each of the
##    three terms are prime, and, (ii) each of the 4-digit numbers are
##    permutations of one another.
##
##    There are no arithmetic sequences made up of three 1-, 2-, or
##    3-digit primes, exhibiting this property, but there is one other
##    4-digit increasing sequence.
##
##    What 12-digit number do you form by concatenating the three
##    terms in this sequence?
