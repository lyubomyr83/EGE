from itertools import product, permutations, repeat


def f1(x, y, z, w):
    return ((x <= y) and (y <= z) and (z <= w))


for a, b, c, d, e in product([0, 1], repeat=5):
    table = (
        (0, a, b, 1, 1),
        (1, c, 0, 1, 1),
        (d, 1, e, 0, 1)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
