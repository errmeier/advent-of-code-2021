import math

count = 0
prev = math.inf

f = open('input.txt', 'r')
depths = [int(line.strip()) for line in f.readlines()]

prev = 0
curr = 3

while curr < len(depths):
    if depths[curr] > depths[prev]:
        count += 1
    prev += 1 
    curr += 1

print(count)
