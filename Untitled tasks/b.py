x=1
while True:
    a = 343 ** 5 + 7 ** 3 - 1 - x
    s = ''
    while a != 0:
        s = str( a % 7 ) + s
        a//= 7 
    if s.count('6') == 12:
        print("x = " , x)
    break
x+=1

