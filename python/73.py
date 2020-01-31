mem = {}
def gcd(a, b):
    if (a, b) in mem:
            return mem[(a, b)]
    while b:
        a, b = b, a % b
        if (a, b) in mem:
            return mem[(a, b)]
    mem[(a, b)] = a
    return a

def is_proper(n, d):
    return gcd(n, d) == 1

ans = 0
den = 1000
for n in range(1, den+1):
    d = 2*n + 1
    if d > den:
        continue
    for x in range(d, 3*n):
        # print n, x
        if is_proper(n, x):
            ans += 1
print ans
