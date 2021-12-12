D = {2: '1', 3: '7', 4: '4', 7: '8'}
O = {'6233': '0', '5122': '2', '5233': '3', '5123': '5', '6123': '6', '6234': '9'}

f = open('input.txt', 'r')
total = 0
for line in f.readlines():
    display_num = ""
    signals, output = line.strip().split('|')
    mapping = {n: set() for n in range(2,5)} 

    # Find letters that correspond to 1, 7, and 4 (strings with len 2, 3, or 4)
    # My solution assumes that each of these patterns occurs at least once.
    # I hypothesize that this is necessary to have enough informatoin to derive a
    # solution but, that might not be the case.
    for pattern in signals.split():
        if len(pattern) in mapping:
            mapping[len(pattern)].update(pattern) 
    
    for comb in output.split():
        # For a length of 2, 3, 4, or 7, there is only one possible digit
        if len(comb) in D:
            display_num += D[len(comb)]

        # Otherwise make a decision based on four numbers:
        # 1. The length of the combination
        # 2. The number of letters the combination has with a 1
        # 3. The number of letters the combination has with a 7
        # 4. The number of letters the combination has with a 4
        # These values together provide a unique identifier for each digit 
        else:
            decision = str(len(comb)) + "".join([str(len(set(comb) & mapping[i])) for i in range(2,5)])
            display_num += O[decision] 
    total += int(display_num)
print(total)
