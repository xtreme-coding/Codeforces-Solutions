for _ in range(int(input())):
    x = input()
    y = int(len(x))
    res = (int(x[0])-1)*10 + (y*(y+1)//2)
    print(res)
