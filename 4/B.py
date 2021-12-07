import sys 
import pprint

class Board:
    def __init__(self):
        self.pos = {}
        self.nums = {}
        self.completed = False

# Read Input
f = open('input.txt', 'r')
selected = f.readline().strip().split(',')
boards = []
target = int(sys.argv[1])
while f.readline() == '\n':
    b = Board()
    for irow in range(5):
        for icol, num in enumerate(f.readline().split()):
            b.pos[num] = (irow, icol)
            b.nums['row'+str(irow)] = b.nums.get('row'+str(irow), []) + [num]
            b.nums['col'+str(icol)] = b.nums.get('col'+str(icol), []) + [num]
    boards.append(b)

solved = 0
score = 0
for s in selected:
    for b in boards:
        if b.completed or s not in b.pos:
            continue
        row, col = b.pos[s]
        b.nums['row'+str(row)].remove(s)
        b.nums['col'+str(col)].remove(s)
        b.pos.pop(s)
        if b.nums['row'+str(row)] == [] or b.nums['col'+str(col)] == []:
            b.completed = True
            score = sum(int(k) for k in b.pos)*int(s)
            solved += 1
            if solved == target:
                print(score)
                sys.exit()

print(score)
