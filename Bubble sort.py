def countSwaps(a):
    # Write your code here
    size = len(a)
    count = 0
    for j in range(size-1):
        for i in range(size-1-j):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                count +=1

       
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[len(a)-1]))