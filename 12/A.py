import sys
import collections

g = collections.defaultdict(list)
for line in sys.stdin:
    source, target = line.strip().split('-')
    g[source].append(target)
    g[target].append(source)

count = 0
neighbors = [('start', ['start'])]
while neighbors:
    node, path = neighbors.pop()
    for n in g[node]:
        if n.islower() and n in path:
            continue
        if n == 'end':
            count += 1
        neighbors.append((n, path + [n]))

print(count)
