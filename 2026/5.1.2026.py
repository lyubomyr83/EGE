for n in range(1, 1000):
    n_bin = bin(n)[2:]
    n_bin += str(sum(map(int, n_bin)) % 2)
    n_bin += str(sum(map(int, n_bin)) % 2)

    if int(n_bin, 2) > 253:
        print(n)
        break