for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    
    dp_positive = [0] * n
    dp_negative = [0] * n

    dp_positive[0] = a[0]
    dp_negative[0] = -a[0]

    for i in range(1, n):
        dp_positive[i] = max(dp_positive[i-1] + a[i], dp_negative[i-1] - a[i])
        dp_negative[i] = max(dp_negative[i-1] + a[i], dp_positive[i-1] - a[i])

    print(max(max(dp_positive),max(dp_negative)))

