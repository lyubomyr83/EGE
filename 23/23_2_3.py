"""
A. Вычти 3
B. Если число чётное, раздели на 2, иначе вычти 5

Сколько существует программ, которые преобразуют исходное число 36 в число 4
и при этом траектория вычислений не содержит числа 16?
"""


def f(start, stop):
    if start == stop:
        return True
    if start < stop or start == 16:
        return False

    return f(start - 3, stop) + (f(start // 2, stop) if start % 2 == 0 else f(start - 5, stop))


print(f(36, 4))
