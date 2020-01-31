from time import time
from itertools import combinations, permutations, product
t = time()

nums = '123456789'
ops = '+- /'
# '(a.)x(b.)y(c.)z(d.)'
brackets = ['(       )          ',
            '(            )     ',
            '(a.)x(b.)y(c.)z(d.)',
            '(a.)x(b.)y(c.)z(d.)',
            '(a.)x(b.)y(c.)z(d.)',
            '(a.)x(b.)y(c.)z(d.)',
            '(a.)x(b.)y(c.)z(d.)']

ans = None

for a,b,c,d in combinations(nums, 4):
    for x,y,z in product(ops, repeat=3):
        pass




print time() - t


'''
By using each of the digits from the set, {1, 2, 3, 4}, exactly once,
and making use of the four arithmetic operations (+, -, *, /) and
brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one
different target numbers of which 36 is the maximum, and each of the
numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest
set of consecutive positive integers, 1 to n, can be obtained, giving your
answer as a string: abcd.'''
