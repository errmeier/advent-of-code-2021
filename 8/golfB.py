O={'6233':'0','2222':'1','5122':'2','5233':'3','4224':'4','5123':'5','6123':'6','3232':'7','7234':'8','6234':'9'}
t = 0
for I in open(0):l,r=I.strip().split('|');m={len(p):set(p) for p in l.split() if len(p) in (2,3,4)};t+=int(''.join(O[str(len(c))+''.join(str(len(set(c)&m[i])) for i in (2,3,4))] for c in r.split()))
print(t)
