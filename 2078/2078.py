pointsmin = 0
pointsmax = 0

def bonus(n1, n2): #создаём функцию для определения бонусных очков
    global pointsmax  #исползуем глобальную переменную
    if n1 == 10:
        pointsmax += 10 + n2
    else:
        pointsmax += n1

F = [int(x) for x in input().split()]

for i in range(len(F)-3):
    if F[i] == 10:
        bonus(F[i+1], F[i+2])

    pointsmin += F[i]
    pointsmax += F[i]
pointsmax += F[7]
pointsmin += F[7]
if F[7] == 10:              #Отдельный подсчёт бонуса для 8 фрейма
    if F[8] == 10:
        if F[9] >= 10:
            pointsmax += 20
        else:
            pointsmax += 10 + F[9]
    else:
        pointsmax += F[8]


pointsmax += F[8]
pointsmin += F[8]


if F[8] == 10:         #Отдельный подсчёт бонуса для предпоследнего фрейма
    if F[9] == 20:
        pointsmax += 20
    elif F[9] > 20:
        pointsmax += 20
        pointsmin += 10
    elif F[9] >= 10:
        pointsmax += F[9]
    else:
        pointsmax += F[9]

pointsmax += F[9]
pointsmin += F[9]

print(pointsmin, '', pointsmax)
