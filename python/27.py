from decimal import *
from time import clock
import euler

# getcontext().prec=2010
t = clock()

a = list(range(-999, 1000))
b = list(range(-999, 1000))
ans = 0
consecutive = 0

for i in a:
    for j in b:
        for n in range(0, 80):
            chk = n*n + i*n + j
            if chk < 2 or not(euler.is_prime(chk)):
                break
            consecutive += 1
        if consecutive > ans:
            ans = consecutive
            coeff_a = i
            coeff_b = j
            # print coeff_a, coeff_b, ans
        consecutive = 0

print(coeff_a, coeff_b, ans, 'answer is', coeff_a * coeff_b)

print('time is', clock()-t)
