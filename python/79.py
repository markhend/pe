from euler import *
from math import factorial
from itertools import permutations
from time import time,clock
t = time()
answer = 0

f = open('keylog.txt', 'r')
l=[]
for line in f:
    l.append(line.strip())
f.close()
l = sorted(list(set(l)))

def is_subseq(sub, full): #substring and full string
    index = 0 #sub index
    for i in full:
        if sub[index] == i:
            index += 1
        if index == len(sub):
            return True
    return False

for i in permutations('01236789'):
    for j in range(len(l)):
##        print l[j], ''.join(i)
        if not is_subseq(l[j], ''.join(i)): break
    if j == len(l)-1:
        print 'answer', ''.join(i)
              
print 'time', time()-t


"""
A common security method used for online banking is to ask
the user for three random characters from a passcode. For example,
if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th
characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible
secret passcode of unknown length
-----
i haven't read all replies, but i found a simple solution: 
determine all digits that occur after a digit in the xyz-codes and you get: 
7=[0, 1, 2, 3, 6, 8, 9], 
3=[0, 1, 2, 6, 8, 9], 
1=[0, 2, 6, 8, 9], 
6=[0, 2, 8, 9], 
2=[0, 8, 9], 
8=[0, 9], 
9=[0] 
0 is always the last digit
-----
RogerHui   (APL/J/K)  
I solved this by hand. The general problem is 
topological sorting, which is to embed a given partial 
order in a linear order. See Donald Knuth's The Art 
of Computer Programming, Volume 1, Section 2.2.3. 
"""
