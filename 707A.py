n, m = map(int, input().split())
a = []
flag = 0
for i in range(n):
    arr = list(map(str, input().split()))
    a.append(arr)
for i in range(n):
    if 'C' in a[i] or 'M' in a[i] or 'Y' in a[i]:
        flag = 1
        break
if flag == 1:
    print('#Color')
else:
    print('#Black&White')
