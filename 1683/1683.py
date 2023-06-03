n = int(input())
layers = []
while n > 1:
    if n//2 < 1:
        val = 1
    else:
        val = n//2
    layers.append(val)
    n -= val
print(len(layers))
print(*layers)

