from bisect import bisect_right

def solve(n, k, a):
    a.sort(reverse=True)
    cnt = [0]*(n+1)
    for i in range(n):
        if a[i] % k == 0:
            cnt[i+1] = cnt[i] + 1
        else:
            cnt[i+1] = cnt[i]
    l, r = 0, n+1
    while r - l > 1:
        mid = (l + r) // 2
        if cnt[bisect_right(a, mid)] * k >= mid:
            l = mid
        else:
            r = mid
    return l

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))