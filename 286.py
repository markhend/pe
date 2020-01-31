from euler import *
from time import time,clock
from math import *

t=time()
total = 0
q = 42.5

def score(x, q):
   return 1 - x/float(q)

for x in range(1,51):
   total += score(x, q)
   print x, total

print total
print time()-t

##   Barbara is a mathematician and basketball player.
##   She has found that the probability of scoring a point
##   when shooting from a distance x is exactly (1 - x/q),
##   where q is a real constant greater than 50.
##
##   During each practice run, she takes shots from
##   distances x = 1, x = 2, ..., x = 50 and, according to
##   her records, she has precisely a 2 percent chance to score
##   a total of exactly 20 points.
##
##   Find q and give your answer rounded to 10 decimal places.
