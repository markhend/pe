from time import time

t = time()
answer = 0
l = []
count = 0
for i in range(1, 250251):
    if i % 250 == 0:
        count += 1
print(2**count % 10**16)

print('time', time() - t)


"""
Find the number of non-empty subsets of {1^1, 2^2, 3^3,..., 250250^250250},
the sum of whose elements is divisible by 250.
Enter the rightmost 16 digits as your answer.
"""
