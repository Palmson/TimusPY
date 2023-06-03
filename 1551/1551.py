n = int(input())
prefectList = []
for i in range(2**n):
    trash, prefect = input().split(' ')
    prefectList.append("".join(prefect))
prefectList.sort()
prefection = {}
for i in prefectList:
    prefection[i] = prefectList.count(i)
m = max(prefection.values())
pref = 2**n
for i in range(n):
    pref//= 2
    if m > pref:
        print(i)
        break
else:
    print(n)
