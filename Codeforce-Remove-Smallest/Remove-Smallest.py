def check_num():
    length = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    checked = False
    if length == 1:
        return "Yes"
    for i in range(length-1):
        if not checked:
            if abs(arr[i]-arr[i+1])>1:
                return "No"
    
    if abs(arr[-1]-arr[-2])>1:
        return "No"
    else:
        return "Yes"
 
t = int(input())
for test_case in range(t):
    print(check_num())
