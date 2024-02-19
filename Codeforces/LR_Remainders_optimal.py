for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
 
    l = 0
    r = n - 1
    prod = 1
    ans = []
 
    for i in range(n - 1):
        if s[i] == 'L':
            l += 1
        else:
            r -= 1
 
    current = a[r]
 
    for i in range(n - 2, -2, -1):
        prod = current % m
        current = current % m
        ans.append(prod)
        if i >= 0:
            if s[i] == 'L':
                l -= 1
                current *= a[l]
            else:
                r += 1
                current *= a[r]
 
    ans.reverse()
 
    for it in ans:
        print(it, end=" ")
 
    print()