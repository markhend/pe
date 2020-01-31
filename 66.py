from math import factorial, sqrt
from time import time
t = time()

squares = {x*x for x in range(1,10**6)}
sol = dict()

for D in range(998,997,-1):
   if D in squares: continue
   print "D is", D,
   x = 1
   while True:
      x += 1
      y2 = divmod((x*x-1), D)
      print y2
      input()
      if y2[0] in squares and y2[1] == 0:
         sol[D] = x
         break
   print "and min_x is", x

print max(sol, key=sol.get)
print 'time', time()-t

'''
Consider quadratic Diophantine equations of the form:
x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x
is 649^2 - 13 x 180^2 = 1.

It can be assumed that there are no solutions in
positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:

3^2 - 2 x 2^2 = 1
2^2 - 3 x 1^2 = 1
9^2 - 5 x 4^2 = 1
5^2 - 6 x 2^2 = 1
8^2 - 7 x 3^2 = 1

Hence, by considering minimal solutions in x for D<=7,
the largest x is obtained when D=5.

Find the value of D<=1000 in minimal solutions of x
for which the largest value of x is obtained.

Tough ones to calc are e.g. 61, 97, 106, 109, 139, 149, 151, 157
1000, 999, 
'''
