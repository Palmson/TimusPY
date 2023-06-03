from sys import stdin

def main():

    m, n = map(int, stdin.readline().split())
    arr = [stdin.readline() for _ in range(n)]
    st = -1
    graph = [0 for _ in range(n * m)]
    per = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                if st == -1:
                    st = i * m + j
                for k in range(4):
                    new_i = i + per[k][0]
                    new_j = j + per[k][1]
                    if 0 <= new_i and new_i < n and 0 <= new_j and new_j < m and arr[new_i][new_j] == '.':
                        graph[i * m + j] |= (1 << k)

    dist = [10 ** 9] * (n * m)
    dq = [0] * n * m
    ind1 = 0
    ind2 = 1
    dq[ind1] = st
    dist[st] = 0
    while ind1 < ind2:
        v = dq[ind1]
        ind1 += 1
        for k in range(4):
            if (1 << k) & graph[v]:
                to = v

                to += per[k][0] * m
                to += per[k][1]
                if dist[to] > dist[v] + 1:
                    dist[to] = dist[v] + 1
                    dq[ind2] = to
                    ind2 += 1

    st = dq[ind1 - 1]
    dist = [10 ** 9] * (n * m)

    ind1 = 0
    ind2 = 1
    dq[ind1] = st
    dist[st] = 0
    ans = 0
    while ind1 < ind2:
        v = dq[ind1]
        ans = max(dist[v], ans)
        ind1 += 1
        for k in range(4):
            if (1 << k) & graph[v]:
                to = v
                to += per[k][0] * m
                to += per[k][1]
                if dist[to] > dist[v] + 1:
                    dist[to] = dist[v] + 1
                    dq[ind2] = to
                    ind2 += 1
    print(ans)

main()