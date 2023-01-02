from collections import defaultdict
nm = [int(i) for i in input().split()]
a = defaultdict(list)
for i in range(nm[0]):
    letter = input()
    a[letter].append(i+1)
for i in range(nm[1]):
    letter2 = input()
    if letter2 in a:
        print(" ".join([str(x) for x in (a[letter2])]))
    else:
        print(-1)
