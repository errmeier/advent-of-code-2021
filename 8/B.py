D = {2: '1', 3: '7', 4: '4', 7: '8'}
O = {'6233': '0', '5122': '2', '5233': '3', '5123': '5', '6123': '6', '6234': '9'}

f = open('input.txt', 'r')
total = 0
for line in f.readlines():
    display_num = ""
    signals, output = line.strip().split('|')
    mapping = {n: set() for n in [2, 3, 4]} 

    for pattern in signals.split():
        if len(pattern) in mapping:
            mapping[len(pattern)].update(pattern) 
    
    for comb in output.split():
        if len(comb) in D:
            display_num += D[len(comb)]
        else:
            decision = str(len(comb)) + "".join([str(len(set(comb) & mapping[i])) for i in range(2,5)])
            display_num += O[decision] 
    total += int(display_num)
print(total)
