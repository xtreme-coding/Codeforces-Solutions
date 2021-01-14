card = input()
pack = list(map(str, input().split()))
flag = 0
for c in pack:
    if c[0] == card[0] or c[1] == card[1]:
        flag = 1
        break
if flag == 1:
    print('YES')
else:
    print('NO')
