import math
h, w, n = map(int, input().split())

line = 0
row = 0

for x in range(n):
    word = input()
    if row == 0:
        row = row + 1
    if line + len(word) <= w:
        line += len(word) + 1
    else:
        line = len(word) + 1
        row += 1
print(math.ceil(row/h)) #round() не подходит :(