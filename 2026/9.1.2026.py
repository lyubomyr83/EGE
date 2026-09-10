"""
Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. Определите количество строк таблицы, содержащих числа, для которых выполнены оба
условия:
– одно число повторяется 3 раза, другое 2 раза, остальные различны;
– максимальное из повторяющихся меньше наибольшего из неповторяющихся.

Ответ:
"""

counter = 0
with open('9.1.txt') as file:
    for line in file.readlines():
       line = list(map(int, line.split()))

       repeat_3 = []
       repeat_2 = []
       not_repeat = []

       unique = set(line)
       for i in unique:
           if line.count(i) == 3:
               repeat_3.append(i)
           elif line.count(i) == 2:
               repeat_2.append(i)
           elif line.count(i) == 1:
                not_repeat.append(i)

       repeat = repeat_3 + repeat_2

       if repeat_3 and repeat_2 and len(not_repeat) == 2:
           if max(repeat) < max(not_repeat):
               counter += 1

print(counter)
