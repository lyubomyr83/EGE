"""
1.  Прибавить 1.
2.  Умножить на 2.

Сколько существует программ, которые преобразуют исходное число 1 в число 16
и при этом никакая команда не повторяется более двух раз подряд?
"""

def f(start, end, k, last_k):
    if start > end:
        return False
    if start == end:
        return True
    if start < end:
        if k == '+' and last_k == '+':
            return  f(start * 2, end, '*', k)
        if k == '*' and last_k == '*':
            return f(start + 1, end, '+', k)
        else:
            return f(start + 1, end, '+', k) + f(start * 2, end, '*', k)

print(f(1, 16, '', ''))
