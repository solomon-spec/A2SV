if __name__ == '__main__':
    n = int(input())
    c = []       
    for i in range(n):
        order = input().split(" ")
        
        if order[0] == "insert":
            c.insert(int(order[1]),int(order[2]))
        elif order[0] == "print":
            print(c)
        elif order[0] == "remove":
            c.remove(int(order[1]))
        elif order[0] == "append":
            c.append(int(order[1]))
        elif order[0] == "sort":
           c.sort()   
        elif order[0] == "pop":
            c.pop()
        if order[0] == "reverse":
            c.reverse()
            
