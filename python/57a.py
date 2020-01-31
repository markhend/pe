count = 0
a, b = 3, 2
for i in range(1000):
    if len(str(a)) > len(str(b)):
        count += 1
    a, b = 2*b+a, a+b
    #print a, b
print count
