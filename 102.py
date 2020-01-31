ans = 0
f = open('triangles.txt', 'r')
lines = [map(int, line.strip().split(',')) for line in f.readlines()]
o = [0, 0]

def slope(ptx, pty):
    if pty[0] == ptx[0]:
        print "divzero"
        return 2000
    return float(pty[1]-ptx[1]) / (pty[0]-ptx[0])

for line in lines:
    a, b, c = line[:2], line[2:4], line[4:]
    
    ab = slope(a, b)
    az = slope(a, o)
    ac = slope(a, c)
    
    ba = slope(b, a)
    bz = slope(b, o)
    bc = slope(b, c)
    
    ca = slope(c, a)
    cz = slope(c, o)
    cb = slope(c, b)
    
    if min(ab, ac) < az < max(ab, ac) and \
           min(ba, bc) < bz < max(ba, bc) and \
           min(ca, cb) < cz < max(ca, cb):
        ans += 1

print ans
