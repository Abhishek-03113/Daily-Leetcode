def miniMaxSum(arr):
    arr.sort()
    a = [arr[i] for i in range(0,len(arr)-1)]
    b = [arr[i] for i in range(1,len(arr))]
    # Write your code here
    print(sum(a))
    print(sum(b))

arr = [1 ,2 ,3 ,4 ,5]

miniMaxSum(arr)