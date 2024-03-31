def find_union(arr1, arr2):
    freq = {}
    union = []
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        union.append(num)
    
    return union


# Driver code

m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = find_union(a, b)

print(ans)
