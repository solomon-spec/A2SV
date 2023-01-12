from collections import defaultdict


t = int(input())
for test_case in range(t):
    nums = []
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    answer = 0
    dic = defaultdict(int)
    
    for rows in range(n):
        rowx =[ int(number) for number in input().split()]
        nums.append(rowx)

    for row in range(n):
        for column in range(m):
            dic["pos"+str(row+column)]+=nums[row][column]
    
    for row in range(n-1,-1,-1):
        for column in range(m):
            dic["neg"+str(row-column)]+=nums[row][column]
            
    for row in range(n):
        for column in range(m):
            if dic["pos"+ str(row+column)] + dic["neg" + str(row-column)]-(nums[row][column]) > answer:
                answer = dic["pos" + str(row+column)] + dic["neg" + str(row-column)] -(nums[row][column])
    print(answer)
