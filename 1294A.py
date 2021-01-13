for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    mval = max(a, b, c)
    n = n-(mval-a)-(mval-b)-(mval-c)
    if n >= 0 and n % 3 == 0:
        print('YES')
    else:
        print('NO')
