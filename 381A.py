n = int(input())
a = list(map(int, input().split()))
count = 1
sum_a, sum_b = 0, 0
while len(a) > 0:
    if count == 1:
        x = max(a[0], a[len(a)-1])
        sum_a += x
        a.pop(a.index(x))
        count = 0
    else:
        y = max(a[0], a[len(a)-1])
        sum_b += y
        a.pop(a.index(y))
        count = 1
print(sum_a, sum_b)
