cubes = [sorted(str(x**3)) for x in range(10000)]
counts = [cubes.count(x) for x in cubes]
print counts.index(5)**3
