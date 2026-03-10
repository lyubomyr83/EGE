from itertools import permutations

table = '24 146 45 12356 34 24'.split() #
graph = 'ab ag bg bc be bd cd ed'.split()

print('1 2 3 4 5 6')

for p in permutations('abcdeg'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)

# 1 2 3 4 5 6
# c d a b g e
# c d g b a e
# e d a b g c
# e d g b a c

# Ответ: 35
