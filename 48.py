''' The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000. '''

ans = 0
for n in range(1, 1001):
    ans += n**n
    ans %= 10**10
print(ans)