def compair():
    n  = int(input())
    for i in range(n):
        lists = input().split(" ")
        if lists[0][-1] =="S":
            no1 = len(lists[0])*(-1)
        elif lists[0][-1]=="M":
            no1 = 0
        else:
            no1 = len(lists[0])
        if lists[1][-1] =="S":
            no2 = len(lists[1])*(-1)
        elif lists[1][-1]=="M":
            no2 = 0
        else:
            no2 = len(lists[1])
        if no1>no2:
            print(">")
        elif no1<no2:
            print("<")
        else:
            print("=")
compair()
