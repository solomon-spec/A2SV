from collections import defaultdict

for x in range(int(input())):
    n = [int(i) for i in input().split()]
    arr =[int(i) for i in input().split()]
    has = defaultdict(int)
    cost = 0
    
    for i in arr:
        has[i]+=1
        
    for i in has:
        if has[i] > n[1]:
            cost+=n[1]
        else:
            cost+=has[i]
            
    print(cost)
