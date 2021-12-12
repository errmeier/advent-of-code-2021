import sys

f = open('input.txt', 'r')
ages = [0]*9
for val in f.readline().split(','):
    ages[int(val)] += 1

for _ in range(int(sys.argv[1])):
    new = ages[0]
    for i in range(len(ages)-1):
        ages[i] = ages[i+1]
    ages[8] = new
    ages[6] += new

print(sum(ages))
