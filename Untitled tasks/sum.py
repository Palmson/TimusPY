a = 20  # определены вне функции
b = 10


def sum():
    c = a + b  # Использование глобальных переменных
    print("Сумма:", c)


def sub():
    d = a - b  # Использование глобальных переменных
    print("Разница:", d)


sum()
sub()