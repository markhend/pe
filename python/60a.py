import euler
# from itertools import permutations
# 3 7 109 673

p = euler.primes(1000000)[1:]    
print len(p)

def chk(a, b):
    return int(str(a) + str(b)) in p and int(str(b) + str(a)) in p

# Add all prime pairs that "chk" True to set s.
s = set()
ln = 200
for i in range(ln):
    for j in range(i+1, ln):
        if chk(p[i], p[j]):
            s.add((p[i], p[j]))
##for i, el in enumerate(s):
##    print el
##    if i > 10: break

res = [[n] for n in p[:ln]]

# start with list of lists, each list is 1 prime
# check all prime pairs up to certain limit
# add 3rd, add 4th, add 5th, return min of sum

for i in range(4):
    print "loop", i
    tmp = []
    for a in res:
        for b in p[p.index(a[-1])+1:ln]:
            if all((x, b) in s for x in a):
                tmp.append(a + [b])
    res = tmp[:]

print res[:10]
