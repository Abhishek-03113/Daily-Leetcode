def missingNumber(arr,n):
        arr.sort()
        for i in range(len(arr)*2):
            if i not in arr and i != 0:
                print(i)
                break
    
arr = [0,-10,1,3,-20]
arr1 = [1,2,3,4,5]
missingNumber(arr1,len(arr1))
missingNumber(arr,len(arr))