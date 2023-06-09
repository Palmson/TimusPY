#Правило Варнсдорфа
#При обходе доски конь следует
#на то поле, с которого можно
#пойти на минимальное число
#ещё не пройденных полей.
#Если таких полей несколько, то
#требуется перебор с возвратом.
n = int(input())
m = n
pos = (0, 0)
x0 = n - int(pos[1])
y0 = ord(pos[0]) - ord('A')
#Суммарное количество клеток доски.
cells_total = n * m
#Инициализация доски.
board = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
#Список допустимых ходов коня.
moves = [(1, 2), (-1, -2),
         (2, 1), (-2, -1),
         (-1, 2), (1, -2),
         (-2, 1), (2, -1)]
#Функция проверки координат
#на соответствие границам доски.
def check_bounds(x, y):
    return -1 < x < n and -1 < y < m
#Функция проверки состояния клетки
#(посещена клетка или еще нет).
def is_visited(x, y):
    return visited[x][y]
#Функция, возвращающая список
#непосещённых клеток доски,
#на которые конь может пойти
#с данной позиции.
def get_move_list(x, y):
    available_moves = []
    for dx, dy in moves:
        xnew, ynew = x + dx, y + dy
        if check_bounds(xnew, ynew):
            if not is_visited(xnew, ynew):
                available_moves.append((xnew, ynew))
    return available_moves
#Рекурсивная функция решения
#задачи о пути коня по доске.
#Возвращает True, если путь
#найден, и False иначе.
def tour(x, y, move_number):
    #Отмечаем текущую клетку
    #как посещенную.
    visited[x][y] = True
    #Если отмечаемый номер соответствует
    #суммарному количеству клеток доски,
    #то возвращаем True (нашли решение).
    answer = False
    if move_number == cells_total - 1:
        board[x][y] = move_number;
        answer = True
    else:
        move_list = get_move_list(x, y)
        if len(move_list) != 0:
            #Получение количества полей,
            #которые доступных с полей
            #из текущего списка.
            neighbors = [ \
                (len(get_move_list(xnew, ynew)), (xnew, ynew)) \
                 for xnew, ynew in move_list]
            #Определение минимального
            #количества полей, доступных
            #с клеток из списка.
            neighbors_min = min([pair[0] for pair in neighbors])
            #Отбор тех полей из списка,
            #с которых можно пойти на
            #минимальное число ещё не
            #пройденных полей.
            canditates = [pair[1] for pair in neighbors \
                          if pair[0] == neighbors_min]
            #Рекурсивно вызываем функцию
            #для каждого из полей-кандидатов,
            #пока не решим задачу или не
            #переберем всех кандидатов.
            for xnew, ynew in canditates:
                if tour(xnew, ynew, move_number + 1):
                    board[x][y] = move_number;
                    answer = True
                    break
    visited[x][y] = False
    return answer
if tour(x0, y0, 0):
    for row in board:
        print(*row)
else:
    print("Нет решения.")