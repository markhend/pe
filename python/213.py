import random
# random.seed(0)
w = h = 30 # grid width and height
grid = [(x,y) for x in range(w) for y in range(h)]
moves = [(1,0), (-1,0), (0,-1), (0,1)]
num_rings = 50 # each ring of bell is one move
n = 21 #num_trials
    
def run_trial():
    for ring in range(num_rings):
        for i,pos in enumerate(grid):
            mv = random.choice(moves)
            chk = (pos[0]+mv[0], pos[1]+mv[1])
            while not (0 <= chk[0] < w and 0 <= chk[1] < h):
                mv = random.choice(moves)
                chk = (pos[0]+mv[0], pos[1]+mv[1])
            grid[i] = chk
    return len(grid) - len(set(grid))

print sum([run_trial() for trial in range(n)]) / float(n)
