from time import time
t = time()

from itertools import count
sieve = {} # {(x = multiple of prime p) >= i: [p, known factor count in x]}
for i in count(2):          # count from 2 upwards
    if i not in sieve:      # if i is prime:
        want = 4            #   want 4 consecutive integers
        p = i
    else:
        p, factors = sieve.pop(i)  # have now noted all factors of i
        if factors < 4:     # non-prime i has less than 4 prime factors
            want = 4
        else:
            want -= 1
            if want == 0:
                print i-3
                break
    # p divides i; find next unoccupied multiple of p in sieve
    while 1:
        i += p
        if i not in sieve: break
        sieve[i][1] += 1    # found one more factor (p) of i
    sieve[i] = [p, 1]       # so far, i has 1 known factor (p)

print time()-t
