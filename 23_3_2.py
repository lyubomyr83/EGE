"""
A.Вычесть 1.
B.Прибавить 3.
C.Умножить на 2.

Сколько существует программ, которые преобразуют исходное число 3 в число 12 и при этом не
содержат двух команд A подряд?
"""

def f(start,end, x):
    if start > end + 1:
        return False
    if start == end:
        return True
    else:
        if x == 1:
            return f(start * 2, end, x-1) + f(start * 3, end, x-1)
        else:
            return f(start -1, end, x+1) + f(start * 2, end, x) + f(start * 3, end, x)


print(f(3,20, 0))
