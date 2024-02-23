def count_zeros_between_ones(sequence):
    count = 0
    zeros_counted = False

    for num in sequence:
        if num == 1:
            if zeros_counted:
                yield count
                count = 0
            zeros_counted = True
        elif num == 0 and zeros_counted:
            count += 1

    yield count 
    
for _ in range(int(input())):
    
    n = int(input()) 
    a = list(map(int, input().split())) 
    
    zero_counts = max(list(count_zeros_between_ones(a)))
    print(zero_counts)

    