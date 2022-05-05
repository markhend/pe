import euler
from itertools import permutations, combinations
from time import time
# 3 7 109 673
# 23 311 677 827
# https://coderwall.com/p/utwriw
# Miller Rabin https://gist.github.com/bnlucas/5857478

t = time()

##p = euler.primes(10**6)
##nums = p[1:167]
         
p = euler.primes(15000000)
nums = p[1:235]
print("p done")

m = {}
def chk(a, b):
    if (a, b) in m:
        return m[(a,b)]
    else:
        m[(a, b)] = int(str(a) + str(b)) in p and int(str(b) + str(a)) in p
        return m[(a, b)]

def solve():
    for a in nums:
        for b in nums[nums.index(a)+1:]:
            if chk(a,b):
                for c in nums[nums.index(b)+1:]:
                    if chk(a,c) and chk(b,c):
                        print(a,b,c)
                        for d in nums[nums.index(c)+1:]:
                            if chk(a,d) and chk(b,d) and chk(c,d):
                                for e in nums[nums.index(d)+1:]:
                                    print(a,b,c,d,e)
                                    if chk(a,e) and chk(b,e) and chk(c,e) and chk(d,e):
                                        return a,b,c,d,e


print(solve())
print(time() - t)
