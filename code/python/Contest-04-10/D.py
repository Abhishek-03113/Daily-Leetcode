"""Ambitious Kid"""

n = int(input())

a = list(map(int, input().split()))

ans = float("inf")

for i in range(n):

    if a[i] < 0:
        ans = min(ans, 0 - a[i])
    else:
        ans = min(ans, a[i])

print(ans)
