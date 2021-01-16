n = int(input())
no = 1
s = 0
while True:
    s += (no*(no+1))//2
    if s > n:
        print(no-1)
        break
    elif s == n:
        print(no)
        break
    no += 1
