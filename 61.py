from time import time
from itertools import product, permutations

t = time()

tri = [n*(n+1)/2 for n in range(45, 141)]
sq = [n*n for n in range(32, 100)]
pen = [n*(3*n-1)/2 for n in range(26, 82)]
hx = [n*(2*n-1)/2 for n in range(32, 101)]
hep = [n*(5*n-3)/2 for n in range(21, 64)]
oc = [n*(3*n-2)/2 for n in range(27, 82)]

def cyc(p):
    for i in range(len(p)-1):
        if str(p[i])[-2:] != str(p[i+1])[:2]:
            return False
        if str(p[-1])[-2:] != str(p[0])[:2]:
            return False
    return True

def solve():
    return next((d, e, f)
                for (a,b,c) in product(tri, sq, pen)
                for (d, e, f) in permutations([a,b,c])
                if cyc([d, e, f]))

print solve()
    
print time() - t
