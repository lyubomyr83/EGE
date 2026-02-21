"""
1.Прибавить 1.
2.Умножить на 2.

Сколько существует программ, которые преобразуют исходное число 2 в число 24 и при этом траектория вычислений содержит
ровно одно из чисел 11 и 12?
"""


def f(start, end):
    if start == end:
        return 1
    if start > end or start == 12:
        return 0
    else:
        return f(start + 1, end) + f(start * 2, end)


def f1(start, end):
    if start == end:
        return 1
    if start > end or start == 11:
        return 0
    else:
        return f1(start + 1, end) + f1(start * 2, end)


print(f1(2, 12) * f1(12, 24) + f(2, 11) * f(11, 24))
