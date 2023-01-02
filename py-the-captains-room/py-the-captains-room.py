from collections import defaultdict
n = int(input())
m = input().split(" ")
o = defaultdict(int)
for i in m:
    o[i]+=1
for i in o:
    if o[i] ==1:
        print(int(i))
        break
