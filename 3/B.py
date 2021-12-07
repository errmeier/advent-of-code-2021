import math

count = 0
ones = [0]*12

f = open('input.txt', 'r')
readings = [line.strip() for line in f.readlines()]

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

root = Node(0)

# Build Tree, left = 0, right = 1
for line in readings:
    curr = root
    for bit in line:
        if bit == '0':
            if curr.left:
                curr = curr.left
                curr.value += 1
            else:
                curr.left = Node(1)
                curr = curr.left
        else:
            if curr.right:
                curr = curr.right
                curr.value += 1
            else:
                curr.right = Node(1)
                curr = curr.right


# O2 rating
curr = root
most_path = ""
while curr == root or (curr and curr.value > 1):
    if not curr.left or not curr.right:
        break

    if curr.left.value > curr.right.value:
        curr = curr.left
        most_path += "0"
    else:
        curr = curr.right
        most_path += "1"

# CO2 rating
curr = root
least_path = ""
while curr == root or (curr and curr.value > 1):
    if not curr.left or not curr.right:
        break

    if curr.left.value > curr.right.value:
        curr = curr.right
        least_path += "1"
    else:
        curr = curr.left
        least_path += "0"

print(most_path)
print(least_path)
print(int(most_path, 2)*int(least_path, 2))
