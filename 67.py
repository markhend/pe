#fp = open('c:/code/67input.txt', 'r')
fp = open('//home/mhenders/Desktop/67input.txt', 'r')
L = []
line = fp.readline()
 
while len(line) != 0:
   #print line,
   L.append(line.rstrip().split(' '))
   line = fp.readline()
"""for line in f:
    L.append(line.split(','))"""
#L.remove([''])

i=0
while i<len(L):
    j=0
    while j<len(L[i]):
        L[i][j] = int(L[i][j])
        #print L[i][j],
        j+=1
    i+=1

i=len(L)-2
while i>=0:
    j=0
    while j<len(L[i]):
        L[i][j] += max(L[i+1][j], L[i+1][j+1])
        j+=1
    i-=1

print 'answer is', L[0][0]



