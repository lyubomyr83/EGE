"""
Для какого наименьшего натурального числа A формула
(y > 10) ∨ (x · A > y + x)
тождественно истинна, то есть принимает значение 1 при любых натуральных x и y?
58
"""

for A in range(1, 1001):
    x_ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((y > 10) or ((x * A) > (y + x))):
                x_ok = False
                break
        if not x_ok:
            break
    else:
        print(A)
        break

