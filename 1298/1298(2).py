n = int(input())
a = [[-1] * n for _ in range(n)]
move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def foo(i, j, pos):
    if pos == n * n:
        return True
    for mi, mj in move:
        i_new = i + mi
        j_new = j + mj
        if 0 <= i_new < n and 0 <= j_new < n and a[i_new][j_new] == -1:
            a[i_new][j_new] = pos
            if foo(i_new, j_new, pos + 1):
                return True
            a[i_new][j_new] = -1
    return False


x = 0
y = 0
a[x][y] = 0
if foo(x, y, 1):
    for row in a:
        print(*row)
else:
    print('IMPOSSIBLE')