from collections import defaultdict
t = int(input())
dic = defaultdict(str)
for _ in range(t):
    x,y,z = input().split()
    dic[x.lower()] = z.lower()
maxx = 0
arr = dic.keys()
for i in arr:
    visited = set()
    word = i
    tot = 0
    while word != "":
        
        if word in dic and word not in visited:
            visited.add(word)
            word = dic[word]
            tot+=1
        else: break
    maxx = max(maxx,tot+1)
print(maxx)
