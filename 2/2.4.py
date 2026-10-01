from itertools import permutations, product

def f(x, y, z, w):
    return (w and(z==(x<=y)))

for a, b, c, d, e in product([0, 1], repeat=5):
    table = (
        (a, b, 0, 0, 1),
        (0, c, d, 0, 1),
        (e, 1, 1, 1, 0)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
