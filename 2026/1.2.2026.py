from itertools import permutations

table = '567 348 278 27 168 15 134 235'.split()
graph = 'AB AE AH BH CE CG CD DF FH FG GE'.split()

print('1 2 3 4 5 6 7 8')

for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)

# 15 + 11 = 26