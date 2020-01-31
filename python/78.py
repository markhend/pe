# http://programmingpraxis.com/2011/04/15/partition-numbers/

def p(n):
    L = [[1]]
    for i in range(1, n + 1):
        L.append([L[x][0] for x in range(i - 1, -1, -1)])
        for j in range((i + 2)/2, i):
            L[j][0] = L[j].pop(0) + L[j][0]
    return sum(L[n]) #not computing all partions, just counting

print p(55374)

##n = 99
##while True:
##    if not (p(n) % 100000):
##        print n
##        break
##    n += 1000

