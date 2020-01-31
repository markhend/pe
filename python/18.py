# fp = open('c:/code/18input.txt', 'r')
f = open('18.txt', 'r')
L = []
for line in f:
    L.append(list(map(int, line.split())))
# print(L)

i = 0
while i < len(L):
    j = 0
    while j < len(L[i]):
        L[i][j] = int(L[i][j])
        # print L[i][j],
        j += 1
    i += 1

i = len(L) - 2
while i >= 0:
    j = 0
    while j < len(L[i]):
        L[i][j] += max(L[i+1][j], L[i+1][j+1])
        j += 1
    i -= 1

print('answer is', L[0][0])
