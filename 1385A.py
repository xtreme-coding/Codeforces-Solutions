for _ in range(int(input())):
    x, y, z = sorted(map(int, input().split()))
    if y < z:
        print('NO')
    else:
        print('YES')
        print(x, x, y)
