n, m, k = map(int,input().split())
arr = []
for _ in range(m):
    arr.append(int(input()))
cur = int(input())
total = 0
for i in arr:
    num = i^cur
    if bin(num).count("1") <= k: total += 1
print(total)


