import math

count = 0
prev = math.inf

f = open('input.txt', 'r')
for line in f.readlines():
    depth = int(line.strip())
    if depth > prev:
        count += 1
    prev = depth

print(count)
