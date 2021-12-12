import math

count = 0
ones = [0]*12

f = open('input.txt', 'r')
for line in f.readlines():
    b = line.strip()
    for i, bit in enumerate(b):
        if bit == '1':
            ones[i] += 1

for i, o in enumerate(ones):
    if o > 500:
        ones[i] = '1'
    else:
        ones[i] = '0'

gamma = int(''.join(ones), 2)
epsilon = int(''.join([str(abs(int(j)-1)) for j in ones]), 2)

print(gamma*epsilon)
