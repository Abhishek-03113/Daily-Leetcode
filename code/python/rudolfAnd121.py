def count_consecutive_same_odds(a):
    max_count = 0
    current_count = 0
    current_num = None
    for num in a:
        if num % 2 == 1:  # num is odd
            if current_num is None or num == current_num:
                current_count += 1
                current_num = num
            else:
                current_count = 1
                current_num = num
            max_count = max(max_count, current_count)
        else:  # num is even
            current_count = 0
            current_num = None
    return max_count

for _ in range(int(input())):
    ans = 0
    n = int(input())
    a = list(map(int, input().split())) 
    
    if count_consecutive_same_odds(a) % 2 == 0: 
        print("YES")
    else:
        print("NO")

    
    