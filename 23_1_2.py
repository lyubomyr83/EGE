"""
A. Вычти 2.
B. Найди целую часть от деления на 2.

Сколько существует программ, для которых при исходном числе 38 результатом является число 2 и при
этом траектория вычислений содержит число 16?
"""


def f(start, stop):
    if start == stop:
        return True
    if start < stop:
        return False

    return f(start - 2, stop) + f(start // 2, stop)

print(f(38, 16) * f(16, 2))
