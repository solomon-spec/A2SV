arr = []
arr=input().split()
def order(x):
    if x.isdigit():
        return ord(x) + 200
    if x.upper() == x:
        return ord(x) + 100
    else:
        return ord(x)

arr.sort(key = lambda y: order(y))
print(arr)