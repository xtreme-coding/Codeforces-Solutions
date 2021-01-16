arr = list(map(int, input().split()))
s = input()
summ = 0
for no in s:
    summ += arr[int(no)-1]
print(summ)
