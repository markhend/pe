num, den = 1, 2
count = 0
for x in xrange(1000):
  if len(str(den+num)) > len(str(den)): count += 1
  num, den = den, 2*den+num
print count
