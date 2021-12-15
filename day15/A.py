import sys
import heapq

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.d = float('inf')

    def add_neighbors_from_grid(self, grid, y, x):
        if y > 0:
            self.neighbors.append(grid[y-1][x])
        if y < len(grid[0])-1:
            self.neighbors.append(grid[y+1][x])
        if x > 0:
            self.neighbors.append(grid[y][x-1])
        if x < len(grid)-1:
            self.neighbors.append(grid[y][x+1])


grid = []
for line in sys.stdin:
    grid.append([Vertex(int(c)) for c in line.strip()])

Q = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x].add_neighbors_from_grid(grid, y, x)

grid[0][0].d = 0
Q = [[grid[y][x].d, y, x] for y in range(len(grid)) for x in range(len(grid[0]))]
heapq.heapify(Q)
while Q:
    d, y, x = heapq.heappop(Q)
    for v in grid[y][x].neighbors:
        if v.d > grid[y][x].d + v.value:
            v.d = grid[y][x].d + v.value
    for t in Q:
        t[0] = grid[t[1]][t[2]].d
    heapq.heapify(Q)

print(grid[len(grid)-1][len(grid[0])-1].d)

    
