import sys

BRACES = {'(': ')', '[': ']', '{': '}', '<':'>'}
ERROR = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in sys.stdin:
    chunks = []
    for c in line.strip():
        if c in BRACES:
            chunks.insert(0, c)
        else:
            if len(chunks) == 0:
                continue
            if BRACES[chunks.pop(0)] != c:
                score += ERROR[c]
                break

print(score)
