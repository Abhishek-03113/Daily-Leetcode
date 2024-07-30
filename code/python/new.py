for _ in range(int(input())):
    
    N = int(input()) 
    A = list(map(int, input().split())) 
    results = []
    from collections import Counter
    freq = list(Counter(A).values())
    total_distinct = len(freq)
    dp = [False] * (N + 1)
    dp[0] = True
    
    for count in freq:
        for j in range(N, count - 1, -1):
            if dp[j - count]:
                dp[j] = True
    
    max_k = 0
    
    for k in range(N, 0, -1):
        if dp[k] and k % total_distinct == 0:
            max_k = k
            break
    
    results.append(max_k)
    
    print(*results)