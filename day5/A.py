import pprint

N = 2048 

def gcd(a, b): 
    if b == 0: 
        return a
    return gcd(b, a%b)

grid = [[0]*N for i in range(N)]

f = open('input.txt', 'r')
for line in f.readlines():
    points = [[int(s) for s in p.split(',')] for p in line.strip().split('->')]
    run = points[1][0] - points[0][0]
    rise = points[1][1] - points[0][1]
    steps = abs(gcd(rise, run))
    run = run//steps
    rise = rise//steps
    x = points[0][0]
    y = points[0][1]
    grid[x][y] += 1
    while x != points[1][0] or y != points[1][1]:
        x += run
        y += rise
        grid[x][y] += 1


count = 0
for row in grid:
    for cell in row:
        if cell > 1:
            count += 1
print(count)
