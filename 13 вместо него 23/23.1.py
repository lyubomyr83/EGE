"""
1. Прибавить 1.
2. Прибавить 2.
3. Умножить на 2.


Сколько существует таких программ, которые исходное число 3 преобразуют в число 12 + Turing и при этом траектория вычислений программы содержит число 10?
"""

def f(start, end):
    if start == end:
        return True
    if start > end:
        return False
    return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)

print(f(3, 10) * f(10, 12))
