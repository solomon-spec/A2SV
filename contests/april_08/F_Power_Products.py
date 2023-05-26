from collections import defaultdict
n,k = map(int,input().split())
arr = list(map(int,input().split()))

def primes(n,k):
    dic = defaultdict(int)
    x = n
    i = 2
    while i*i <= n:
        if x % i == 0:
            dic[i] += 1
            x //= i
        else:
            i += 1
    if x != 1: dic[x]+= 1
    ans = []
    for i in dic:
        if dic[i] % k != 0:
            ans.append((i,dic[i] % k))
    ans.sort(key = lambda x: x[0])
    ans2 = [(i,-dic[i] % k) for i,j in ans]
    return tuple(ans),tuple(ans2)
di2 = defaultdict(int)
ans = 0
for i in arr:
    x = primes(i,k)
    ans += di2[x[1]]
    di2[x[0]] += 1
print(ans)
