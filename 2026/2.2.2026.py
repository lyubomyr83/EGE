from itertools import product, permutations

def f1(x, y, z, w):
    return ((x and not(z) and not(w)) or (x and not(z) and y))


for a, b, c, d, e, f, g in product([0,1], repeat=7):
    table = (
    (1, a, b, c, 1),
    (0, d, 1, e, 1),
    (f, g, 0, 0, 1)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)