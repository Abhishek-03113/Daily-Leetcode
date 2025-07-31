def solve():
    n = int(input())
    b = list(map(int, input().split()))
    
    min_val = min(b)
    
    # Find the first position where we start having only min_val elements till the end
    suffix_start = n
    for i in range(n - 1, -1, -1):
        if b[i] == min_val:
            suffix_start = i
        else:
            break
    
    # Check if the prefix (before suffix_start) is non-decreasing
    for i in range(suffix_start - 1):
        if b[i] > b[i + 1]:
            print("NO")
            return
    
    # If all conditions pass, we can build it greedily
    print("YES")

for _ in range(int(input())):
    solve()
