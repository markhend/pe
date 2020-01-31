import euler
from itertools import permutations, combinations
from time import time
# 3 7 109 673
# 23 311 677 827

t = time()

##p = euler.primes(10**6)
##nums = p[1:167]
         
p = euler.primes(15000000)
nums = p[1:235]

# print len(p)

##def chk(a, b):
##    return int(str(a) + str(b)) in p and int(str(b) + str(a)) in p

m = {}
def chk(a, b):
    if (a, b) in m:
        return m[(a,b)]
    else:
        m[(a, b)] = int(str(a) + str(b)) in p and int(str(b) + str(a)) in p
        return m[(a, b)]

##s = {(a, b) for (a, b) in combinations(nums, 2) if chk(a, b)}
##print "s built"

##for a in nums:
##    for b in nums[nums.index(a)+1:]:
##        if chk(a, b):
##            for c in nums[nums.index(b)+1:]:
##                if all(chk(x, y) for (x, y) in combinations((a, b, c), 2)):
##                    for d in nums[nums.index(c)+1:]:
##                        if all(chk(x, y) for (x, y) in combinations((a, b, c, d), 2)):
##                            print a,b,c,d

##def solve():
##    return next((a,b,c,d)
##                for a in nums
##                for b in nums[nums.index(a)+1:]
##                if chk(a, b)
##                for c in nums[nums.index(b)+1:]
##                if all(chk(x, y) for (x, y) in combinations((a, b, c), 2))
##                for d in nums[nums.index(c)+1:]
##                if all(chk(x, y) for (x, y) in combinations((a, b, c, d), 2)))

##def solve():
##    return next((a,b,c,d)
##                for (a,b,c,d) in combinations(nums, 4)
##                if chk(a,b) and chk(a,c) and chk(a,d)
##                and chk(b,c) and chk(b,d) and chk(c,d))
##def solve():
##    return next((a,b,c,d,e) for (a,b,c,d,e) in combinations(nums, 5)
##                if all(chk(x, y) for (x,y) in combinations((a,b,c,d,e), 2)))

def solve():
    return next((a,b,c,d,e)
                for (a,b,c,d,e) in combinations(nums, 5)
                if chk(a,b) and chk(a,c) and chk(a,d) and chk(a,e)
                and chk(b,c) and chk(b,d) and chk(b,e)
                and chk(c,d) and chk(c,e) and chk(d,e))


print solve()
print time() - t
