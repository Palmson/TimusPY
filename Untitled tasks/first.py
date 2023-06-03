def numberous(n):
    numbers = ['few', 'several', 'pack', 'lots', 'horde', 'throng', 'swarm', 'zounds', 'legion']
    if n == 0:
        n = 21
    elif 1 <= n < 5:
        print(numbers[0])
    elif n < 10:
        print(numbers[1])
    elif n < 20:
        print(numbers[2])
    elif n < 50:
        print(numbers[3])
    elif n < 100:
        print(numbers[4])
    elif n < 250:
        print(numbers[5])
    elif n < 500:
        print(numbers[6])
    elif n < 1000:
        print(numbers[7])
    elif n >= 1000:
        print(numbers[8])

nume = int(input())
numberous(nume)

