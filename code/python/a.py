import sys

sys.setrecursionlimit(10**9)

n, x = map(int, input().split())

a = list(map(int, input().split()))


inf = float("inf")


dp = [inf] * (x + 1)
dp[0] = 0
ans = inf

for i in range(1, x+1):

    for j in a:
        if j > i or dp[i - j] == inf:
            continue

        else:
            dp[i] = min(dp[i], dp[i - j] + 1)

if dp[x] != inf:
    print(dp[x])
else:
    print(-1)
