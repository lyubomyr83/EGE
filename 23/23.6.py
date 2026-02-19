"""
1.  Прибавить 1.
2.  Умножить на 2.

Сколько существует программ, для которых при исходном числе 1 результатом является число 21,
при этом траектория вычислений содержит число 10 и не содержит число 17?
"""

def f(start, stop):
    if start == stop:
        return True
    if start > stop + 1 or start == 17:
        return False

    return f(start + 1, stop) + f(start * 2, stop)

print(f(1, 10) * f(10, 21))
