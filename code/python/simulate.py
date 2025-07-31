from collections import deque

def simulate_moves(p, moves):
    """Simulate the moves and show the result"""
    dq = deque(p)
    result = []
    
    print(f"Initial: {list(dq)}")
    
    for i, move in enumerate(moves):
        if move == 'L':
            val = dq.popleft()
            result.append(val)
            print(f"Step {i+1}: L -> took {val}, remaining: {list(dq)}, result: {result}")
        else:  # move == 'R'
            val = dq.pop()
            result.append(val)
            print(f"Step {i+1}: R -> took {val}, remaining: {list(dq)}, result: {result}")
    
    print(f"Final result: {result}")
    return result

# Test what RRRLLLL gives us
p1 = [1, 2, 3, 4, 5, 6, 7]
expected_moves = "RRRLLLL"
print("Expected moves:", expected_moves)
result = simulate_moves(p1, expected_moves)

# Check if this result is good
def is_bad_sequence(seq):
    if len(seq) < 5:
        return False
    for i in range(len(seq) - 4):
        if all(seq[j] < seq[j+1] for j in range(i, i+4)):
            return True
    for i in range(len(seq) - 4):
        if all(seq[j] > seq[j+1] for j in range(i, i+4)):
            return True
    return False

print(f"Is result bad? {is_bad_sequence(result)}")
