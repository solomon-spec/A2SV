for _ in range(int(input())):
    word = input()
    if word[-1] != "B" or word[0] == "B": print("NO")
    else:
        t = True
        stack = []
        for i in word:
            if i == "A": stack.append("A")
            else:
                if not stack: 
                    print("NO")
                    t = False
                    break
                else: stack.pop()
        if t: print("YES")
            