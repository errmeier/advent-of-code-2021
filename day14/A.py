import sys
import collections

polymer = sys.stdin.readline().strip()
sys.stdin.readline()

rules = {}
counts = collections.defaultdict(int)
for line in sys.stdin:
    pattern, insert = line.strip().split(' -> ')
    rules[pattern] = insert

start = polymer[0]
end = polymer[-1]
for i in range(len(polymer)-1):
    counts[polymer[i:i+2]] += 1

for _ in range(10):
    new_counts = counts.copy()
    for c in counts:
        if counts[c] == 0:
            continue
        if c in rules:
            new_counts[c[0] + rules[c]] += counts[c]
            new_counts[rules[c] + c[1]] += counts[c] 
            new_counts[c] -= counts[c] 
    counts = new_counts

single_counts = collections.defaultdict(int)
for pattern in counts:
    single_counts[pattern[0]] += counts[pattern]
    single_counts[pattern[1]] += counts[pattern]
single_counts = sorted([(single_counts[pattern]+1)//2 for pattern in single_counts])
print(single_counts[-1] - single_counts[0])

    
    
