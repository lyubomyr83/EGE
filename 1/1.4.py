from itertools import permutations

from jinja2.nodes import Break

table = '56 4568 78 2578 1246 125 348 2347'.split() #
graph = 'АБ АГ АЕ БГ БЖ БД ГЕ ГЖ ЖД ЖИ ИД ИВ ВД'.split()

print('1 2 3 4 5 6 7 8')

for p in permutations('АБВГДЕЖИ'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)


# Ж 2/4
# Д 5/8
# 4-8
# Ответ: 19