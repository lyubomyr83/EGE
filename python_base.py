# функция для перевода в систему счисления ниже 10-тичной
def convert(n, to):
    answer = '' # ответ

    while n > 0:
        answer += str(n % to)  # прибавляем к answer остаток от деления n на основание системы счисления
        n = n // to

    return answer[::-1]

print(convert(23, 7))