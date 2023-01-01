def setunion():
    n = input()
    english = set(input().split(" "))
    m  = input()
    french = set(input().split())
    print(len(english.union(french)))
    
setunion()
