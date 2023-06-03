def scheduling(m):
    index = list(range(len(m)))
    max_set = set()
    prev_event_time = 0
    for i in index:
        if m[i][1] >= prev_event_time:
            max_set.add(i)
            prev_event_time = m[0][i]

    return max_set

n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))
m.sort(key=lambda x: x[0])
result = scheduling(m)
print(len(result))





