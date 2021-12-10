import sys

BRACES = {'(': ')', '[': ']', '{': '}', '<':'>'}
ERROR = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in sys.stdin:
    chunks = []
    for c in line.strip():
        if c in BRACES:
            chunks.insert(0, c)
        else:
            if BRACES[chunks.pop(0)] != c:
                chunks = []
                break

    if not chunks:
        continue

    row_score = 0
    for b in chunks:
        row_score *= 5
        row_score += ERROR[b]
    scores.append(row_score)

print(scores)
print(sorted(scores)[len(scores)//2])
