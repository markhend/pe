from decimal import *
from time import clock

getcontext().prec=2010
t = clock()

max_cycle = 6
for i in range(2,1000):
    s = str(1 / Decimal(i))[2:]
    x = 6
    no_max_results = 0
    if len(s) > 5:
        for j in range(6,1001):
            if s[x:x+j] == s[x+j:x+j+j]:
                no_max_results += 1
                if no_max_results > 1 or j == 6: break
                if j > max_cycle:
                    max_cycle = j
                    answer_d = i
                    
print 'time is', clock()-t
print 'answer_d is', answer_d, 'max_cycle is', max_cycle



   
        
