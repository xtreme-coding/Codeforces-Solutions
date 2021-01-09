n = int(input())
print(n//2)
a = [2]*(n//2-1)
print(*a, n % 2+2)
