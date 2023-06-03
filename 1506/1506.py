n, k = map(int, (input().split()))
F = [int(x) for x in input().split()]
if n % k != 0:
    stroke = n//k + 1
else:
    stroke = n//k
for i in range(stroke):
    for j in range(i, len(F), stroke):
        print('%4d' % (F[j]), end='')
    print(end='\n')
