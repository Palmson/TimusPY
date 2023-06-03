x, y, z = map(int, input().split())
left = 0
right = 0
down = 0
up = 0
back = 0
forward = 0
for val in input():
    if val == 'd':
        down = max(0, down-1)
        up += 1
    elif val == 'u':
        up = max(0, up-1)
        down += 1
    elif val == 'l':
        left = max(0, left-1)
        right += 1
    elif val == 'r':
        right = max(0, right-1)
        left += 1
    elif val == 'b':
        back = max(0, back-1)
        forward += 1
    elif val == 'f':
        forward = max(0, forward-1)
        back += 1
print(max(1, x-(left+right))*max(1, y-(down+up))*max(1, z-(back+forward)))
