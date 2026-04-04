
for A in range(100, 0, -1):
    col = 0
    for s, t in ((-9,11), (2,7), (5,12), (2,-2), (7,-9), (12,6), (9,-1), (7,11), (11,-5)):
        if (s > A) or (t > 11):
           col += 1
    if col == 6:
        print(A)
        break
