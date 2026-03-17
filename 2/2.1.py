from itertools import product, permutations

def func(x, y, z, w):
    return (z or (z == w) or (not (y <= x)))

# Заменили f на h в списке переменных, чтобы не затирать функцию func
for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    table = ((a, b, 0, 1, 0),
             (c, 1, d, 0, 0),
             (e, 0, f, g, 0))

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(func(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
