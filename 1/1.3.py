from itertools import permutations

table = '25 156 45 357 123467 257 456'.split() #
graph = 'КА КБ КВ  КГ КД КЕ АБ БВ ВГ ГД ДЕ'.split()

print('1 2 3 4 5 6 7')

for p in permutations('АБВГДЕК'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)

# 1 2 3 4 5 6 7
# А Б Е Д К В Г
# Е Д А Б К Г В

# 2-6, 4-7

# Ответ: 13 + 7 = 20