def check_strict():
    a = set(input().split(" "))
    hashtable = {i:j for j, i in enumerate(a)}
    n = int(input())
    x = 1
    def check():
        for i in range(n):
            b = set(input().split(" "))
            if len(b)>=len(a):
                return False
            for number in b:
                if number not in hashtable:
                    return False
        return True
    print(check())    
        
check_strict()
            
