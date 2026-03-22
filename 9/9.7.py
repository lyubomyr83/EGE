"""
В каждой строке электронной таблицы записаны шесть натуральных чисел.
Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:

— в строке есть число, повторяющееся не меньше трёх раз;
— в строке есть число, не повторяющееся в этой строке;
— среднее арифметическое всех повторяющихся чисел строки (с учётом количества повторений) меньше среднего арифметического неповторяющихся чисел этой строки.

В ответе запишите число — количество строк, удовлетворяющих заданным условиям
"""

lines = open('9.7.txt').readlines()

col = 0
for line in lines:
    line = list(map(int, line.split()))
    ok = False

    for n in line:
        if line.count(n) >= 3:  # первая проверка
            for n in line:
                if line.count(n) == 1:  # вторая проверка
                    repeat = []
                    not_repeat = []

                    for n in line:
                        if line.count(n) > 1:
                            repeat.append(n)
                        else:
                            not_repeat.append(n)

                    if (sum(repeat) / len(repeat)) < (sum(not_repeat) / len(not_repeat)):  # третья проверка
                        ok = True
                        col += 1
                if ok:
                    break
        if ok:
            break

print(col)
