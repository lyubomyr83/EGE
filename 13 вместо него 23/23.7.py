"""
1.Прибавь 1.
2.Прибавь 3.
3.Прибавь предыдущее.

Сколько существует программ, которые число 2 преобразуют в число 10?
"""

def f(start, stop):
    if start == stop:
        return True
    if start > stop:
        return False

    return f(start + 1, stop) + f(start + 3, stop) + f(start + start - 1, stop)

print(f(2, 10))
