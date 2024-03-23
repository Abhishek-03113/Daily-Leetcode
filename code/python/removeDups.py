def removeDuplicates(arr,n):

    l, r = 0, 1 

    while r < n: 

        if arr[l] != arr[r]: 
            l += 1 
            r += 1 
        elif arr[l] == arr[r]:
            while r < n and arr[l] != arr[r]: 
                r+=1
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp 
        
    print(arr)

n = int(input())
arr = list(map(int, input().split()))

removeDuplicates(arr, n)
