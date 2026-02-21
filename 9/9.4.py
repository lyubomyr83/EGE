"""
Определите, сколько среди заданных троек чисел таких, которые могут быть сторонами прямоугольного треугольника
"""

count = 0
data = open("9.2.txt")
for line in data.readlines():
    a, b, c = [int(i) for i in line.split()]
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        count += 1
print(count)
