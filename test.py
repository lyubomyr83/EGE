from itertools import permutations, product

def f1(x, y, z, w):
    return ((w == (not(z == y))) and (z == (y <= x)))

for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    table = ((a, 0, 0, b, 1), (c, 0, d, 0, 1), (e, f, g, 0, 1))

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)


