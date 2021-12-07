import statistics

f = open('input.txt', 'r')
data = [int(x) for x in f.readline().strip().split(',')]
m = statistics.median(data)
print(sum([abs(x-m) for x in data]))


