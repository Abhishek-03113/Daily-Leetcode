t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    w.sort(reverse=True)
    max_weight = 0
    for i in range(n):
        max_weight = max(max_weight, w[i]*(i+1))
    print(max_weight)