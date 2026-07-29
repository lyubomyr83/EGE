"""
Определите количество пятизначных чисел, записанных в девятеричной системе счисления,
в записи которых ровно две цифры 3, и при этом никакая нечётная цифра не стоит рядом с
цифрой 2.

"""
from operator import index


def convert(n):
    answer = ''
    while n > 0:
        answer += str(n % 9)
        n = n // 9
    return answer[::-1]

col = 0

for i in range(10000, 100000):
    i_ = convert(i)
    if i_.count('3') == 2:
        for j in i_:
            if j == '2':
                if