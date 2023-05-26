for _ in range(int(input())):
    word = input()
    w = sorted(list(word))
    x = "".join(w) + "".join(reversed(w))
    print(x)
