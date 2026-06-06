"""
Сколько можно составить девятеричных пятизначных чисел таких,
чтобы в них все цифры были различны и была только одна нечетная цифра?
"""

from itertools import permutations

col = 0
for p in permutations('012345678', 5):
    if p[0] != '0':
        if len(set(p)) == len(p):
            nechet_col = 0
            for i in ('1', '3', '5', '7'):
                if i in p:
                    nechet_col += 1

            if nechet_col == 1:
                col += 1

print(col)
