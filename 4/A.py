import sys 

class Board:
    def __init__(self):
        self.pos = {}
        self.nums = {}

# Read Input
f = open('input.txt', 'r')
selected = f.readline().split(',')
boards = []
while f.readline() == '\n':
    b = Board()
    for irow in range(5):
        for i, num in enumerate(f.readline().split()):
            b.pos[num] = (irow, i)
            b.nums['row'+str(irow)] = b.nums.get('row'+str(irow), []) + [num]
            b.nums['col'+str(i)] = b.nums.get('col'+str(i), []) + [num]
    boards.append(b)

for s in selected:
    for b in boards:
        if s not in b.pos:
            continue
        row, col = b.pos[s]
        b.nums['row'+str(row)].remove(s)
        b.nums['col'+str(col)].remove(s)
        b.pos.pop(s)
        if b.nums['row'+str(row)] == [] or b.nums['col'+str(col)] == []:
            print(sum(int(k) for k in b.pos)*int(s))
            sys.exit()
