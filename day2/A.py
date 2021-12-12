f = open('input.txt', 'r')

horiz = 0
vert = 0
for line in f.readlines():
    direction, magn = line.strip().split()
    magn = int(magn)
    if direction == 'forward':
        horiz += magn
    elif direction == 'down':
        vert += magn
    else:
        vert -= magn

print(horiz*vert)
