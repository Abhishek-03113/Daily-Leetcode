def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    def is_1122(freq_map):
        """Check if the current frequency map satisfies the 1122 condition."""
        for count in freq_map.values():
            if count != 0 and count != 2:
                return False
        return True
    
    left = 0
    freq_map = {}
    max_len = 0

    for right in range(N):
        # Include A[right] in the current window
        freq_map[A[right]] = freq_map.get(A[right], 0) + 1
        
        # Ensure the window is valid
        while not is_1122(freq_map):
            # Remove A[left] from the window
            freq_map[A[left]] -= 1
            if freq_map[A[left]] == 0:
                del freq_map[A[left]]
            left += 1
        
        # Update max_len if the current window is valid
        if is_1122(freq_map):
            max_len = max(max_len, right - left + 1)
    
    print(max_len)

solve() 

def calculateWomanSalary(MenSalary):
    return 