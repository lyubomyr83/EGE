x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

for y in range(y1,y2+1):
    print(f'\t{y}', end='')

for x in range(x1,x2+1):
    print(f'\n{x}', end='')
    for y in range(y1, y2 + 1):
        print(f'\t{x*y}', end='')