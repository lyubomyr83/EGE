"""
В каждой строке электронной таблицы записаны шесть натуральных чисел.
Определите количество строк таблицы, содержащих числа,
для которых одновременно выполнены все следующие условия:

— в строке есть число, повторяющееся не меньше трёх раз
— в строке есть число, не повторяющееся в этой строке
— среднее арифметическое всех повторяющихся чисел строки (с учётом количества повторений)
больше среднего арифметического неповторяющихся чисел этой строки

В ответе запишите число — количество строк, удовлетворяющих заданным условиям.
"""

data = open('9.6.txt')

counter = 0
for line in data.readlines():
    line = line.split()
    repeat_3 = False
    for n in line:
        if line.count(n) >= 3:
            repeat_3 = True
            break

    if repeat_3:
        repeat_1 = False
        for n in line:
            if line.count(n) == 1:
                repeat_1 = True
                break

        if repeat_1:
            repeat = []
            not_repeat = []

            for n in line:
                if line.count(n) == 1:
                    not_repeat.append(int(n))
                else:
                    repeat.append(int(n))

            if sum(repeat)/len(repeat) > sum(not_repeat)/len(not_repeat):
                counter += 1

print(counter)