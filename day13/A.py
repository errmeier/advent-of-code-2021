import sys

points = set() 
folds = []
for line in sys.stdin:
    if line == '\n':
        continue
    if ',' in line:
        points.add(tuple(map(int, line.strip().split(','))))
    else:
        direction, value = line.strip().split('=')
        folds.append(('x' if 'x' in direction else 'y', int(value))) 


for f in folds:
    if f[0] == 'x':
        points = {(2*f[1]-p[0], p[1]) if p[0] >= f[1] else (p[0], p[1]) for p in list(points)}
    else:
        points = {(p[0], 2*f[1]-p[1]) if p[1] >= f[1] else (p[0], p[1]) for p in list(points)}
    break

print(len(points))


