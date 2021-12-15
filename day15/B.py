import sys
import heapq

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.d = float('inf')

    def __lt__(self, other):
        return self.d < other.d

    def add_neighbors_from_grid(self, grid, y, x):
        if y > 0:
            self.neighbors.append(grid[y-1][x])
        if y < len(grid)-1:
            self.neighbors.append(grid[y+1][x])
        if x > 0:
            self.neighbors.append(grid[y][x-1])
        if x < len(grid[0])-1:
            self.neighbors.append(grid[y][x+1])

def increment(x, i):
    x += i
    if x > 9:
        return x % 9 
    return x

grid = []
for line in sys.stdin:
    grid.append([Vertex(increment(int(c), k)) for k in range(5) for c in line.strip()])

nrows = len(grid)
ncols = len(grid[0])
for k in range(1,5):
    for j in range(nrows):
        grid.append([Vertex(increment(grid[j][i].value, k+r)) for r in range(5) for i in range(ncols)])

for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x].add_neighbors_from_grid(grid, y, x)

grid[0][0].d = 0
Q = [(0, grid[0][0])]
visited = set()
count = 0
while Q:
    d, u = heapq.heappop(Q)
    if u in visited:
        continue
    visited.add(u)
    for v in u.neighbors:
        if v.d > u.d + v.value:
            v.d = u.d + v.value
        heapq.heappush(Q, (v.d, v))

print(grid[len(grid)-1][len(grid[0])-1].d)

    
