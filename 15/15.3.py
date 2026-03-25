p = list(range(15, 41))
q = list(range(21, 64))
all_a = []

for A in range(1000):
    for x in range(1000):
        if not((x in p) <= (((x in q) and (not(x in all_a))) <= (not(x in p)))):
            break
    else:
        all_a.append(A)

print(all_a)