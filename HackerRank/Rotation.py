def rotation(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr





for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    for i in range(k):
        arr = rotation(arr)
    print(*arr)


    