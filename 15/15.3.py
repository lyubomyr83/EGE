P = list(range(15, 41))
Q = list(range(21, 64))
A = list(range(1, 1000))
for x in range(1, 1000):
    if not((x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))):
        break
else:
    print(A)

# Ответ 19