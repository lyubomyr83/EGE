"""
A. Вычесть 1.
B. Прибавить 3.
C. Умножить на 2.

Сколько существует программ, которые преобразуют исходное число 3 в число 12 и
при этом не содержат двух команд A подряд?
"""


def f(start, end, command):
    if start == end:
        return True
    if start > end + 1:
        return False

    if command == 1:
        return f(start + 3, end, command - 1) + f(start * 2, end, command - 1)
    else:
        return f(start -1 , end, command + 1) + f(start + 3, end, command) + f(start * 2, end, command)


print(f(3, 12,0))
