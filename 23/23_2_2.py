"""
A. Вычесть 1.
B. Прибавить 3.
C. Умножить на 2.

Сколько существует программ, которые преобразуют исходное число 3 в число 12 и
при этом не содержат двух команд A подряд?
"""


def f(start, end, ok):
    if start == end:
        return True
    if start > end + 1:
        return False

    if ok:
        return f(start + 3, end, False) + f(start * 2, end, False)
    else:
        return f(start -1 , end, True) + f(start + 3, end, ok) + f(start * 2, end, ok)


print(f(3, 12,False))
