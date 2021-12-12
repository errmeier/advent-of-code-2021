import sys
import collections

g = collections.defaultdict(list)
for line in sys.stdin:
    source, target = line.strip().split('-')
    g[source].append(target)
    g[target].append(source)

count = 0
neighbors = [('start', ['start'], 2)]
while neighbors:
    node, path, doubled = neighbors.pop()
    for n in g[node]:
        if n == 'start' or (n.islower() and path.count(n) >= doubled):
            continue
        if n == 'end':
            print(','.join(path + [n]))
            count += 1
            continue
        if n.islower() and n in path:
            neighbors.append((n, path + [n], 1))
        else:
            neighbors.append((n, path + [n], doubled))

print(count)
