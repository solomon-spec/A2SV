def insertionSort1(n, ar):

    arr = [str(i) for i in ar]
    cur = arr[-1]
    j  = len(arr)-1
    while j>0 and cur < arr[j-1]:
        arr [j] = arr[j-1]
        j -= 1
        print(" ".join(arr))
    arr[j] = cur
    print (" ".join(arr))
