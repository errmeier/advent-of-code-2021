f = open('input.txt', 'r')
count = 0
for line in f.readlines():
    signals, output = line.strip().split('|')
    for comb in output.split():
        if (len(comb) >= 2 and len(comb) <= 4) or len(comb) == 7:
            count += 1
print(count)
