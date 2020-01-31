s = '''131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331'''

a = [[0 for _ in range(5)] for _ in range(5)]
s = s.split()
n = 0
for i in range(5):
    for j in range(5):
        a[i][j] = int(s[n])
        n += 1
print a
    
