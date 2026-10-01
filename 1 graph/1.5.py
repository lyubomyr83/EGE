from itertools import permutations

table = '578 478 457 237 136 58 1234 126'.split()
graph = 'аб аг ае бв бг вд ви ге дж еж жи'.split()

print('1 2 3 4 5 6 7 8')

for p in permutations('абвгдежи'):
    if all(str(p.index(x) + 1) in table[p.index(y)] for x, y in graph):
        print(*p)
