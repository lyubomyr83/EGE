from itertools import permutations

table = '56 679 578 89 138 127 236 345 24'.split() #
graph = 'АБ АЕ АГ БВ ВД ВК ДК ДГ ГЕ ЕЖ ЖИ ИК'.split()

print('1 2 3 4 5 6 7 8 9')

for p in permutations('АБВГДЕЖИК'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)

# 1 2 3 4 5 6 7 8 9
# Б Е Д И В А Г К Ж
# Б К Г Ж А В Д Е И

# Ответ: 37
