# -*- coding: cp1252 -*-
from euler import *
from math import *
from itertools import permutations
from time import time,clock
t = time()
answer = 0

##ways = 0
##x = 200 #goal
##
##for a in range(x,-1,-1):
##   for b in range((x-a)/2,-1,-1):
##      for c in range((x-a-2*b)/5,-1,-1):
##         for d in range((x-a-2*b-5*c)/10,-1,-1):
##            for e in range((x-a-2*b-5*c-10*d)/20,-1,-1):
##               for f in range((x-a-2*b-5*c-10*d-20*e)/50,-1,-1):
##                  for g in range((x-a-2*b-5*c-10*d-20*e)/100,-1,-1):
##                     for h in range((x-a-2*b-5*c-10*d-20*e-50*f)/200,-1,-1):
##                        if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h == x:
##                           ways += 1
##print 'ways is', ways

#see bottom for links to explanations
vals = [1]+[0]*200
for coin in [1,2,5,10,20,50,100,200]:
   for i in range(coin,201):
      #print vals[i], '+=', vals[i-coin]
      vals[i] += vals[i-coin]
print vals[200]

print 'time', time()-t



"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
-----------------------------------------------------------------
After failing to solve this problem myself,
I discovered that there are many published solutions on the internet,
most of which have been repeated here. The best discussion
I could find is:
   
http://www.algorithmist.com/index.php/Coin_Change

Which at the bottom gives a link to a complete discussion
of the dynamic programming solution: 

http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf 

I'm not sure which makes this site more valuable:
the education I receive or the humility that I learn.
"""
