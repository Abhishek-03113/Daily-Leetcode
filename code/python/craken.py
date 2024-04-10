from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sunk = 0

    while k > 0 and len(a) > 0:
        if a[0] > 0:
            a[0] -= 1
            if a[0] == 0:
                a.pop(0)
                sunk += 1
        k -= 1
        if k > 0 and len(a) > 1 and a[-1] > 0:
            a[-1] -= 1
            if a[-1] == 0:
                a.pop()
                sunk += 1
            k -= 1

    print(sunk)
