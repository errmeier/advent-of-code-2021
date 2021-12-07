data = [int(x) for x in open('input.txt','r').read().strip().split(',')]
print(min(sum(((abs(x-m)*(abs(x-m)+1))//2 for x in data)) for m in range(max(data))))
