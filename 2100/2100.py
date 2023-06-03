n = int(input())
c = 2 + n
for i in range(n):
    s = str(input())
    c += s.count('+one')
if c == 13:
    c += 1
print(c*100)
