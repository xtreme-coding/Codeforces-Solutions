for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s, odd, even = 0, 0, 0
    for x in a:
        s = (s+x) % 2
        if x % 2 == 1:
            odd += 1
        else:
            even += 1
    if s % 2 == 1:
        print('YES')
        continue
    if odd != n and even != n:
        print('YES')
        continue
    print('NO')
