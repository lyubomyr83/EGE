from itertools import *
def func(x, y, z):
    return  ((x == z) or (x <= (y and z)))

for a, b, c in product([0, 1], repeat=3):
    table = ((0,0,a,0),
             (1,b,c,0))
    if len(table) == len(set(table)):
        for p in permutations("xyz"):
            if all(func(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
