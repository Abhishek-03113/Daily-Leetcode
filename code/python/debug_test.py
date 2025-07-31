from collections import deque

def is_bad_sequence(seq):
    """Check if sequence contains 5 consecutive increasing or decreasing elements"""
    if len(seq) < 5:
        return False
    for i in range(len(seq) - 4):
        if all(seq[j] < seq[j+1] for j in range(i, i+4)):
            return True
    for i in range(len(seq) - 4):
        if all(seq[j] > seq[j+1] for j in range(i, i+4)):
            return True
    return False

def solve_debug(p):
    """Debug version with detailed output"""
    print(f"Initial permutation: {p}")
    dq = deque(p)
    result = []
    moves = []
    step = 0
    
    while dq:
        step += 1
        left = dq[0] if dq else None
        right = dq[-1] if dq else None
        
        print(f"\nStep {step}:")
        print(f"  Current deque: {list(dq)}")
        print(f"  Current result: {result}")
        print(f"  Left option: {left}, Right option: {right}")
        
        if left is not None:
            temp_result_left = result + [left]
            left_makes_bad = len(temp_result_left) >= 5 and is_bad_sequence(temp_result_left)
            print(f"  Adding left ({left}) would give: {temp_result_left}")
            print(f"  Left makes bad: {left_makes_bad}")
        
        if right is not None:
            temp_result_right = result + [right]
            right_makes_bad = len(temp_result_right) >= 5 and is_bad_sequence(temp_result_right)
            print(f"  Adding right ({right}) would give: {temp_result_right}")
            print(f"  Right makes bad: {right_makes_bad}")
        
        if left is not None and not left_makes_bad:
            dq.popleft()
            result.append(left)
            moves.append('L')
            print(f"  Chose LEFT: {left}")
        elif right is not None and not right_makes_bad:
            dq.pop()
            result.append(right)
            moves.append('R')
            print(f"  Chose RIGHT: {right}")
        else:
            # Both would make bad sequence, choose left by default
            if left is not None:
                dq.popleft()
                result.append(left)
                moves.append('L')
                print(f"  Both bad, chose LEFT: {left}")
            elif right is not None:
                dq.pop()
                result.append(right)
                moves.append('R')
                print(f"  Both bad, chose RIGHT: {right}")
        
        if step > 10:  # Safety break
            break
    
    print(f"\nFinal result: {result}")
    print(f"Final moves: {''.join(moves)}")
    print(f"Expected: RRRLLLL")
    return ''.join(moves)

# Test case 1
p1 = [1, 2, 3, 4, 5, 6, 7]
solve_debug(p1)
