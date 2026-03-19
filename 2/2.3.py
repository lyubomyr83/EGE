from itertools import *


def f1(x, y, z, w):
    return ((x <= y) == (w or (not(z))))


def f2(x, y, z, w):
    return (x <= y) and ((not (w)) == z)


for a, b, c, d, e in product([0, 1], repeat=5):
    table = ((a, 1, 0, 1, b, 0),
             (c, 0, 0, 0, 0, d),
             (0, e, 0, 0, 0, 1))

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, line[:-2]))) == line[-2] and f2(**dict(zip(p, line[:-1]))) == line[-1] for line in
                   table):
                print(*p)
