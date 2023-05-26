for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    summ = (x*(x+1))//2
    for i in arr:
        if i<= x: summ -= i*2
    print(summ)