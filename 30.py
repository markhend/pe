from euler import *
from time import time,clock

t=time()

##count,answer=0,0
##for i in range(4000,200000):
##    sum=0
##    for j in str(i):
##        sum += (int(j))**5
##    if i==sum:
##        print i
##        count += 1
##        answer += sum
##print count
##print answer

answer=0
for num in xrange(2,200000):
    if num == sum(int(i)**5 for i in str(num)):
        answer += num
print answer

print time()-t

"""one liner:
print sum(i for i in range(2,1000000) if i==sum(int(j)**5 for j in str(i)))
"""
