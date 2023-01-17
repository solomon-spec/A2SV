def countSwaps(a):
    swap = 0
    for x in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swap += 1
    print("Array is sorted in {} swaps.".format(swap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
