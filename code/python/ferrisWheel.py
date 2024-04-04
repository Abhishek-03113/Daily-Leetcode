n, x = map(int, input().split())

ans = 0

a = list(map(int, input().split()))

a.sort()

# i = 1
# while i < n:
#     if a[i] + a[i - 1] <= x:
#         i += 2
#         ans += 1
#     else:
#         ans += 2
#         i += 1
# print(ans)

pt1 = 0
pt2 = n - 1

while pt1 < pt2:
    if a[pt1] + a[pt2] <= x:
        a[pt2] += a[pt1]
        pt1 += 1
        pt2 -= 1
    else:
        pt2 -= 1

print(n - pt1)
