for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    for item in a:
        if item not in arr:
            arr.append(item)
    print(*arr)
