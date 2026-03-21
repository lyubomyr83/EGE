print(sum([int(i) for i in iter(input, "0") if int(i) % 8 == 0 and len(i) == 2]))
