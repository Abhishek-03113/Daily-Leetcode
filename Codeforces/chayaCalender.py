t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    y = a[0]

    for i in range(1, n):
        if a[i] > y:
            y = a[i]
        else:
            j = 1
            temp = a[i]
            while a[i] <= y:
                a[i] = temp * j
                j += 1
            y = a[i]
    print(y)
