"""
Значение арифметического выражения
5 * 7776**2013 + 4 * 1296**2015 − 3 * 216**2017 + 2 * 36**2017 − 6 **2019 + 2021
записали в 36-ричной системе счисления. Определите сумму цифр больших 9 в этой записи.

"""

answer = 5 * 7776**2013 + 4 * 1296**2015 - 3 * 216**2017 + 2 * 36**2017 - 6 **2019 + 2021

digits = list(range(10, 36))
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet = dict(zip(digits, letters)) # {10: 'A', 11: 'B'}}
alphabet_2 = {y: x for x, y in alphabet.items()} # {'A': 10, 'B': 11}


def convert(n, to):
    ost = ''

    while n > 0:

        ost += str(alphabet[n % to] if n % to > 9 else n % to)
        n = n // to
    return ost[::-1]

converted = convert(answer, 36)
s = 0

for i in converted:
    if i.isalpha():# если буква
        s += alphabet_2[i]

print(s)