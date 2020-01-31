from time import time
t = time()

f = open('keylog.txt')
attempts = set(l.strip() for l in f)
 
G = {}
for (x,y,z) in attempts:
    for c in (x,y,z):
        if not c in G:
            G[c] = set()
    G[y].add(x)
    G[z].add(y)
 
# Now repeatedly remove the node without outgoing arcs
sol = []
while len(G) > 0:
    empty = [x for x in G if not G[x]][0]
    sol.append(empty)
    del G[empty]
    for x in G:
        G[x].discard(empty)
 
print ''.join(sol)
print 'time', time()-t

"""
I first did it by hand, but I thought it would be nice to
code it too. I make a graph of all the triplets, i.e. '730'
means the edges 0->3 and 3->7 get added. After that, there
should be only one node without outgoing edges,
this is the first digit, remove it and the edges to it,
and find the second digit, et cetera.
"""
