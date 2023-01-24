a = input()
nums1 = input().split()
nums2 = input().split()
pt1 = 0
pt2 = 0
answer = []
while pt1<len(nums1) and pt2 < len(nums2):
    if int(nums1[pt1]) > int(nums2[pt2]):
        answer.append(nums2[pt2])
        pt2 += 1
    else:
        answer.append(nums1[pt1])
        pt1 += 1
        
answer +=(nums1[pt1:]+nums2[pt2:])
print(" ".join(answer))
