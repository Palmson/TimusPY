import math
n, r = input().split()
n = int(n)
r = float(r)
X = []
Y = []
S = 2 * 3.14 * r
for i in range(n):
    x, y = map(float, (input().split()))
    X.append(x)
    Y.append(y)
    if i > 0:
        S += math.sqrt((X[i] - X[i - 1]) ** 2 + (Y[i] - Y[i - 1]) ** 2)
S += math.sqrt((X[len(X) - 1] - X[0]) ** 2 + (Y[len(Y) - 1] - Y[0]) ** 2)
print(S)
