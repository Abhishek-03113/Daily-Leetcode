# for _ in range(int(input())):
#     n, k = map(int, input().split())

#     ks = []
#     for _ in range(k):
#         l, r, m = map(int, input().split())
#         ks.append((l, r, m))

#     ans = [n] * n
#     flg = True 
    
    

#     for l, r, m in ks:
#         l -= 1;r -= 1

#         if ans[l] <= m:
#             if m > 1:
#                 ans[l] = m - 1
#             else:
#                 flag = False
#                 for i in range(l, r + 1):
#                     if ans[i] == m:
#                         flag = True
#                         if m + 1 <= n:
#                             ans[i] = m + 1
#                         break
#                 if not flag:
#                     flg = False
#                     break

#     if flg:
#         for l, r, m in ks:
#             l -= 1
#             r -= 1
#             if ans[l] == m:
#                 flg = False
#                 break

#     if flg:
#         print(*ans)
#     else:
#         print(-1)
for _ in range(int(input())):
    n, k = map(int, input().split())
    ks = [tuple(map(int, input().split())) for _ in range(k)]
    arr = [n] * n
    flg = True
    for l, r, m in ks:
        l -= 1
        r -= 1
        if min(arr[l:r + 1]) <= m:
            if m > 1:
                arr[l] = m - 1
            else:
                flag = False
                for i in range(l, r + 1):
                    if arr[i] == m:
                        if m + 1 <= n:
                            arr[i] = m + 1
                        flag = True
                        break
                if not flag:
                    flg = False
                    break
    if flg:
        for l, r, m in ks:
            l -= 1
            r -= 1
            if min(arr[l:r + 1]) == m:
                flg = False
                break
    if flg:
        print(*arr)
    else:
        print(-1)
