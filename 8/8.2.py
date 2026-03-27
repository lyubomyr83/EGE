"""
Определите количество 12-ричных пятизначных чисел, в записи которых
ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8
"""

from itertools import product

col = 0
for i in product("0123456789AB", repeat=5):
    # Проверка: первая цифра не должна быть "0"
    if i[0] != "0":
        if i.count("7") == 1:
            # Считаем количество цифр > 8 (9, A, B)
            big_digits = i.count("9") + i.count("A") + i.count("B")
            if big_digits <= 3:
                col += 1

print(col)
