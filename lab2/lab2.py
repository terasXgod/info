inp = input()

for x in inp:
    if x not in '01':
        print("Ошибко: Поддерживается только ввод чисел: 0, 1")
        exit()


if len(inp) > 7:
    print("Ошибко: Кажется ты добавил лишних битов")
    exit()
elif len(inp) < 7:
    print("Ошибко: Кажется ты потерял пару битов")
    exit()

a = list(map(int, inp))
s1 = (a[0] + a[2] + a[4] + a[6]) % 2
s2 = (a[1] + a[2] + a[4] + a[5]) % 2
s3 = (a[3] + a[4] + a[5] + a[6]) % 2
s = 4 * s3 + 2 * s2 + s1
if s != 0:
    a[s-1] = (a[s-1] + 1) % 2

    bits = ['r1', 'r2', 'i1', 'r3', 'i2', 'i3', 'i4']

    print(f"{a[2]}{a[4]}{a[5]}{a[6]}")
    print(f"Ошибко была в бите {bits[s-1]}: {(a[s-1] + 1) % 2} -> {a[s-1]}")
else:
    print(f"{a[2]}{a[4]}{a[5]}{a[6]}")
    print(f"Ошибко не найдено")