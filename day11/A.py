import sys

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbors_from_grid(self, grid, y, x):
        for j in (y-1, y, y+1):
            for i in (x-1, x, x+1):
                if i == x and y == j:
                    continue
                if i >= 0 and i < len(grid[0]) and j >= 0 and j < len(grid):
                    self.neighbors.append(grid[j][i])

def flash(grid):
    flashing = []
    nflashes = 0
    for row in grid:
        for v in row:
            v.value += 1
            if v.value == 10:
                flashing.append(v)
                nflashes += 1

    while flashing:
        v = flashing.pop(0)
        for n in v.neighbors:
            n.value += 1
            if n.value == 10:
                flashing.append(n)
                nflashes += 1

    for row in grid:
        for v in row:
            if v.value > 9:
                v.value = 0

    return nflashes


grid = []
for line in sys.stdin:
    grid.append([Vertex(int(c)) for c in line.strip()])

for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x].add_neighbors_from_grid(grid, y, x)

print(sum(flash(grid) for _ in range(100)))
