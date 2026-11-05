"""
Для какого наибольшего целого неотрицательного числа A логическое выражение
(x + y ≤ 33) ∨ (y ≤ x + 9) ∨ (y ≥ A)
тождественно истинно (т.е. принимает значение 1) при любых целых положительных x и y ?
"""

for A in range(1000, 0, -1):
    x_ok = True

    for x in range(1, 1001):
        for y in range(1, 1001):
            if not ((x + y <= 33) or (y <= x + 9) or (y >= A)):
                x_ok = False
                break

        if not x_ok:
            break

    else:
        print(A)
        break

