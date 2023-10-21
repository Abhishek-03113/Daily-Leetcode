t = int(input())

while(t!=0):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    count = 0
    for i in range(n):
        for j in range(n):
            for v in range(i,n):
                for k in range(j,n):
                    if arr[i][j]>arr[v][k]:
                        count+=1
    print(count)

    t-=1