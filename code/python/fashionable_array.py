def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Count even and odd numbers
    even_count = sum(1 for x in a if x % 2 == 0)
    odd_count = n - even_count
    
    # The maximum fashionable subarray is the larger group
    max_fashionable_size = max(even_count, odd_count)
    
    # Minimum operations = total elements - max fashionable size
    return n - max_fashionable_size

t = int(input())
for _ in range(t):
    print(solve())
