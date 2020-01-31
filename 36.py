from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0

##def ispalindromic(s):
##    return all(s[i]==s[-i-1] for i in range(len(s)/2))

for i in xrange(1000000):
    dec = str(i)
    if dec[-1]=='0':continue
    binary = str(bin(i))[2:]
    if binary[-1]=='0':continue
    if dec==dec[::-1] and binary==binary[::-1]:
##    if ispalindromic(dec) and ispalindromic(binary):
        print dec, binary
        answer+=i
        
print "answer is", answer
print time()-t

##The decimal number, 585 = 1001001001 (binary),
##is palindromic in both bases.
##Find the sum of all numbers, less than one million,
##which are palindromic in base 10 and base 2.
##(Please note that the palindromic number,
##in either base, may not include leading zeros.)

##def rotate(L, N):
##       return L[N:] + L[:N]
