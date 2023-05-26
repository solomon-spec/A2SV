from collections import defaultdict, deque
alien_dict  = []
impos = False
n = int(input())
for _ in range(n):
    alien_dict.append(input())
arr = defaultdict(int)
dic = defaultdict(list)
for i in range(26): arr[chr(97 + i)] = 0
for i in range(1,len(alien_dict)):
    minn = min(len(alien_dict[i-1]),len(alien_dict[i]))
    found = False
    for j in range(minn):
        if alien_dict[i][j] != alien_dict[i -1][j]:
            dic[alien_dict[i-1][j]].append(alien_dict[i][j])
            arr[alien_dict[i][j]] += 1
            arr[alien_dict[i-1][j]] = arr[alien_dict[i-1][j]]
            found = True
            break;
    if not found:
        if len(alien_dict[i-1]) > len(alien_dict[i]): impos = True

queue = deque()
for i in arr:
    if arr[i] == 0: queue.append(i)
ans = [] 
while queue:
    x = queue.popleft()
    ans.append(x)
    for i in dic[x]:
        arr[i] -= 1
        if arr[i] == 0: queue.append(i)

if impos or len(ans) != 26: print("Impossible")
else: print("".join(ans))