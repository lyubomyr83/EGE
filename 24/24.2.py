"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, состоящей из символов X.
Хотя бы один символ X находится в последовательности
"""
data = open('24.2.txt').readline()

# 1 решение с помощью регулярных выражений
from re import findall
all_ = findall(r'X{1,}', data) #  {n}, {n, m}, {n,}, {,m} - количество повторений
print(len(max(all_)))

# 2 решение с помощью цикла
max_counter = 0
counter = 1
for i in range(len(data) - 1):
    if data[i] == "X" and data[i + 1] == "X":
        counter += 1
    else:
        if counter > max_counter:
            max_counter = counter
        counter = 1
print(max_counter)
