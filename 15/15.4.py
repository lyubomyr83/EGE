"""
Для какого наибольшего целого неотрицательного числа
логическое выражение

(x * y > A) V (x>y) V (11 > x)

тождественно истинно (т.е. принимает значение 1) при любых целых неотрицательных x и y
?
"""

for A in range(1000, 0, -1):
    ok = True
    for x in range(100):
        for y in range(100):
            if not((x * y > A) or (x > y) or (11 > x)):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        break
