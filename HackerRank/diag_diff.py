n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

def diagonalsum(arr):
    n = len(arr)
    suml = 0
    sumr = 0    
    diagl = [ arr[i][i] for i in range(n) ]
    diagr = [arr[i][n-i-1] for i in range(n)]
    suml =sum(diagl)
    sumr = sum(diagr)


    return suml,sumr

print(diagonalsum(arr))