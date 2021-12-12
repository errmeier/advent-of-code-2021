import sys

grid = []
for line in sys.stdin:
    row = [int(c) for c in line.strip()] 
    grid.append(row)

low_points = []
for n in range(len(grid)):
    for i in range(len(grid[0])):
        if n > 0 and grid[n][i] >= grid[n-1][i]:
                continue
        if n < len(grid)-1 and grid[n][i] >= grid[n+1][i]:
                continue
        if i > 0 and grid[n][i] >= grid[n][i-1]:
                continue
        if i < len(grid[0])-1 and grid[n][i] >= grid[n][i+1]:
                continue
        low_points.append((n, i))

basins = [0]*len(low_points)
for b, (n, i) in enumerate(low_points):
    visited = set()
    neighbors = [(n,i)]
    while neighbors:
        row, col = neighbors.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if grid[row][col] == 9:
            continue
        print(grid[row][col], end=" ")
        basins[b] += 1
        if row > 0 and (row-1, col) not in visited:
            neighbors.append((row-1, col))
        if row < len(grid)-1 and (row+1, col) not in visited:
            neighbors.append((row+1, col))
        if col > 0 and (row, col-1) not in visited:
            neighbors.append((row, col-1))
        if col < len(grid[0])-1 and (row, col+1) not in visited:
            neighbors.append((row, col+1))

    print()

basins = sorted(basins, reverse=True)
print(basins[0]*basins[1]*basins[2])
