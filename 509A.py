n = int(input())
arr = [[0]*n]*n
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
print(arr[n-1][n-1])
