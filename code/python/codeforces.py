import bisect

def solve():
    # Read number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read n (number of cells), m (number of teachers), q (number of queries)
        n, m, q = map(int, input().split())
        
        # Read the positions of the teachers
        teacher_positions = list(map(int, input().split()))
        teacher_positions.sort()
        
        david_positions = list(map(int, input().split()))
        
        
        for david_pos in david_positions:
            idx = bisect.bisect_left(teacher_positions, david_pos)
            
            min_moves = float('inf')
            
            if idx == 0:
                min_moves = teacher_positions[idx] - 1  # Move to the left
            
            if idx > 0:
                min_moves = min(min_moves, abs(david_pos - teacher_positions[idx - 1]))
            
            if 0< idx < m:
                min_moves = min(min_moves, abs(david_pos - teacher_positions[idx]))
            
            print(min_moves)

# Driver code to execute the solution
solve()
