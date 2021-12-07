f = open('input.txt', 'r')

horiz = 0
vert = 0
aim = 0

for line in f.readlines():
    direction, magn = line.strip().split()
    magn = int(magn)
    if direction == 'forward':
        horiz += magn
        vert += aim*magn
    elif direction == 'down':
        aim += magn
    else:
        aim -= magn

print(horiz*vert)
