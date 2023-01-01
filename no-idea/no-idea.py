def counthappines():
    m= input()
    n = input().split(" ")
    a= set(input().split(" "))
    b=set(input().split(" "))
    happ = 0
    for num in n:
        if num in a:
            happ+=1
        if num in b:
            happ-=1
    print(happ)
counthappines()
  
      
