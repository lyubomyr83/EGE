"""
Определите количество пятизначных чисел, записанных в девятеричной системе счисления,
в записи которых ровно две цифры 3, и при этом никакая нечётная цифра не стоит рядом с
цифрой 2.

Ответ:3352

Внимательно читать условие!!! Число сначала переводится в девятиричную СС а потом считается его длина
"""


def convert(n):
    answer = ''
    while n > 0:
        answer += str(n % 9)
        n = n // 9
    return answer[::-1]

col = 0

for i in range(100000):
    i_ = convert(i)
    if len(i_) == 5:
        if i_.count('3') == 2:

            ok = True

            for j in range(5):
                if i_[j] == '2':
                    if 0 < j < 4:
                        if i_[j-1] not in ['1', '3', '5', '7'] and i_[j+1] not in ['1', '3', '5', '7']:
                            pass
                        else:
                            ok = False
                            break
                    elif j == 0:
                        if i_[j + 1] not in ['1', '3', '5', '7']:
                            pass
                        else:
                            ok = False
                            break
                    elif j == 4:
                        if i_[j-1] not in ['1', '3', '5', '7']:
                            pass
                        else:
                            ok = False
                            break

            if ok:
                col += 1

print(col)