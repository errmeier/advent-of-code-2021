D={2:'1',3:'7',4:'4',7:'8'}
O={'6233':'0','5122':'2','5233':'3','5123':'5','6123':'6','6234':'9'}
t = 0
for I in open(0):l,r=I.strip().split('|');m = {len(p):set(p) for p in l.split() if len(p) in (2,3,4)};t+=int(''.join(D[len(c)] if len(c) in D else O[str(len(c))+''.join(str(len(set(c)&m[i])) for i in (2,3,4))] for c in r.split()))
print(t)
