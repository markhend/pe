''' Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904
are reversible. Leading zeroes are not allowed in either n or reverse(n).
There are 120 reversible numbers below one-thousand.
How many reversible numbers are there below one-billion (10**9)?
'''
cnt = 0
odds = set("13579")
test = []

# for n in range(10**3):
#     if n % 10 == 0:
#         continue
#     r = int(str(n)[::-1])
#     # r = int(''.join(reversed(str(n))))
#     ok = True
#     for c in str(n + r):
#         if c not in odds:
#             ok = False
#             break
#     if ok:
#         test.append(n+r)
#         cnt += 1
#         # print("n", n, "r", r, end=' | ')


def num_to_list(n):
    L = []
    while n:
        L.append(n % 10)
        n //= 10
    return L


def reversible(n):
    L = num_to_list(n)
    carry = 0
    for x, y in zip(L, L[::-1]):
        tmp = x + y + carry
        if tmp % 2 == 0:
            return False
        carry = tmp // 10
    return True

ans = 0
for n in range(1, 500001):
    if reversible(n):
        ans += 1
print(n, ans)

