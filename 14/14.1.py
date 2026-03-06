"""
Значение выражения 36^7 + 6^19 − 18 записали в системе счисления с основанием 6.
Сколько цифр 0 содержится в этой записи?
"""

def convert(n, to):
    answer = ''
    while n > 0:
        answer += str(n % to)
        n = n // to
    return answer[::-1]

print(convert(36**7 + 6**19 - 18, 6).count('0'))
