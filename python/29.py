from euler import *
from time import time,clock

t=time()
##L = []
set1 = set()
for i in range(2,101):
    for j in range(2,101):
##        L.append(i**j)
        set1.add(i**j)

##print len(set(L))
print len(set1)

print time()-t
