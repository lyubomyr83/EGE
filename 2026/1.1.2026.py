from itertools import permutations

table = '234 148 18 127 67 578 456 236'.split()
graph = 'AF AH AG BC BH BE DG DC DE EH FG'.split()

print('1 2 3 4 5 6 7 8')

for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)

# Ответ 23
