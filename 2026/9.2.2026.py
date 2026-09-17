"""Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел. Определите наименьший номер строки, для которой выполнены оба условия:
– все числа в строке различны;
– удвоенная сумма максимального и минимального больше суммы остальных трех чисел.
"""

file = open('9.2.txt')



for num, line in enumerate(file.readlines(), start=1):
    line = sorted(list(map(int, line.split())))
    # print(line)
    if len(set(line)) == len(line):
        if (2 * (line[0] + line[-1])) > sum(line[1:4]):
            print(num)
            break
