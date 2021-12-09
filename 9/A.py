import sys

grid = []
for line in sys.stdin:
    row = [int(c) for c in line.strip()] 
    grid.append(row)

total = 0
count = 0
low_points = []
for n in range(len(grid)):
    for i in range(len(grid[0])):
        if n > 0:
            if grid[n][i] >= grid[n-1][i]:
                continue
        if n < len(grid)-1:
            if grid[n][i] >= grid[n+1][i]:
                continue
        if i > 0:
            if grid[n][i] >= grid[n][i-1]:
                continue
        if i < len(grid[0])-1:
            if grid[n][i] >= grid[n][i+1]:
                continue
        count += 1
        low_points.append(grid[n][i])
        total += grid[n][i] + 1

print(low_points)
print(count)
print(total)
