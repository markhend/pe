def is_prime(n):
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


def ispan(s):
    if sorted(s)[:len(s)] == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'][:len(s)]:
        return True
    else:
        return False


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    tmp = a * b
    while b:
        a, b = b, a % b
    return tmp / a


def euler_sieve(n):
 # Create a candidate list within which non-primes will
 # marked as None, noting that only candidates below
 # sqrt(n) need be checked.
    candidates = range(n + 1)
    fin = int(n**0.5)
 # Loop over the candidates, marking out each multiple.
 # If the current candidate is already checked off then
 # continue to the next iteration.
    for i in range(2, fin + 1):
        if not candidates[i]:
            continue
        candidates[2 * i::i] = [None] * (n // i - 1)
 # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]


def primes(n):
    # t=clock()
    s = range(0, n + 1)
    s[1] = 0
    bottom = 2
    top = n // bottom
    while (bottom * bottom <= n):
        while (bottom <= top):
            if s[top]:
                s[top * bottom] = 0
            top -= 1
        bottom += 1
        while s[bottom] == 0:
            bottom += 1
        top = n // bottom
    # print 'time', clock()-t
    return [x for x in s if x]


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def is_subseq(sub, full):  # substring and full string
    index = 0  # sub index
    for i in full:
        if sub[index] == i:
            index += 1
        if index == len(sub):
            return True
    return False


def fib(n):
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[n]


def factors(n):
    p = primes(n)
    l = []
    while n not in p:
        for i in p:
            if i > n / 2:
                break
            if n % i == 0:
                n = n / i
                l.append(i)
    l.append(n)
    return l


"""
def fac(n):
    return reduce(lambda x,y: x*y, range(1,n+1), 1)
    
def fa(n):
    if n in d:
      return d[n]
    if n == 0:
      return 1
    d[n] = n * fa(n-1)
    return fa(n)
    
def rotate(L, N):
       return L[N:] + L[:N]

m = max(d, key=d.get)

for i,n in enumerate(iterable[, start]):
    
letters = 'abcdefghijklmnopqrstuvwxyz'
pos = {letters[i-1]:i for i in range(1,27)}

fp = open("42words.txt", 'r')
tmp = fp.read()
words = [word.strip('"') for word in tmp.split(',')]

int(''.join(str(i) for i in num))

[(x,y) for x in a for y in a]
"""
