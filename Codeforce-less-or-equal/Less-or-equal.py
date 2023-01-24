nm = input().split()
n = int(nm[0])
m = int(nm[1])
 
nums = [int(i) for i in input().split()]
 
nums.sort()
if m > len(nums):
    print(-1)
elif m == len(nums):
    print(nums[-1])
elif m == 0:
    h = nums[0]-1 if nums[0]>1 else -1
    print(h)
else:
    if nums[m-1] != nums[m]:
        print(nums[m-1])
    else:
        print(-1)
