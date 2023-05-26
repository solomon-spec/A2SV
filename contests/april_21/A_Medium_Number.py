t = int(input())
for i in range(t):
    array = list(map(int,input().split()))
    array.sort()
    print(array[1])