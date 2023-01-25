a = input()
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
n = len(nums1)
m = len(nums2)
left = 0
for i in range(m):
    while left < n and  nums1[left] < nums2[i]:
        left +=1
    nums2[i] = left
print(*nums2)
    
