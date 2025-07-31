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

def solve_debug_detailed(p):
    """Debug version with very detailed output"""
    print(f"Initial permutation: {p}")
    dq = deque(p)
    result = []
    moves = []
    step = 0
    
    while dq:
        step += 1
        if len(dq) == 1:
            result.append(dq.popleft())
            moves.append('L')
            print(f"Step {step}: Only one left, chose L")
            break
            
        left = dq[0]
        right = dq[-1]
        
        print(f"\nStep {step}:")
        print(f"  Current deque: {list(dq)}")
        print(f"  Current result: {result}")
        print(f"  Left option: {left}, Right option: {right}")
        
        temp_result_left = result + [left]
        left_makes_bad = len(temp_result_left) >= 5 and is_bad_sequence(temp_result_left)
        
        temp_result_right = result + [right]
        right_makes_bad = len(temp_result_right) >= 5 and is_bad_sequence(temp_result_right)
        
        print(f"  Left makes bad: {left_makes_bad}")
        print(f"  Right makes bad: {right_makes_bad}")
        
        if left_makes_bad and not right_makes_bad:
            dq.pop()
            result.append(right)
            moves.append('R')
            print(f"  Only left bad -> chose RIGHT: {right}")
        elif right_makes_bad and not left_makes_bad:
            dq.popleft()
            result.append(left)
            moves.append('L')
            print(f"  Only right bad -> chose LEFT: {left}")
        elif left_makes_bad and right_makes_bad:
            dq.popleft()
            result.append(left)
            moves.append('L')
            print(f"  Both bad -> chose LEFT: {left}")
        else:
            print(f"  Both safe, checking patterns...")
            if len(result) >= 4:
                last_4 = result[-4:]
                is_increasing = all(last_4[i] < last_4[i+1] for i in range(3))
                is_decreasing = all(last_4[i] > last_4[i+1] for i in range(3))
                print(f"  Last 4: {last_4}, increasing: {is_increasing}, decreasing: {is_decreasing}")
                
                if is_increasing:
                    print(f"  Breaking increasing pattern...")
                    if left <= result[-1]:
                        dq.popleft()
                        result.append(left)
                        moves.append('L')
                        print(f"  Left breaks pattern -> chose LEFT: {left}")
                    elif right <= result[-1]:
                        dq.pop()
                        result.append(right)
                        moves.append('R')
                        print(f"  Right breaks pattern -> chose RIGHT: {right}")
                    else:
                        if left < right:
                            dq.popleft()
                            result.append(left)
                            moves.append('L')
                            print(f"  Both continue, chose smaller LEFT: {left}")
                        else:
                            dq.pop()
                            result.append(right)
                            moves.append('R')
                            print(f"  Both continue, chose smaller RIGHT: {right}")
                elif is_decreasing:
                    print(f"  Breaking decreasing pattern...")
                    if left >= result[-1]:
                        dq.popleft()
                        result.append(left)
                        moves.append('L')
                        print(f"  Left breaks pattern -> chose LEFT: {left}")
                    elif right >= result[-1]:
                        dq.pop()
                        result.append(right)
                        moves.append('R')
                        print(f"  Right breaks pattern -> chose RIGHT: {right}")
                    else:
                        if left > right:
                            dq.popleft()
                            result.append(left)
                            moves.append('L')
                            print(f"  Both continue, chose larger LEFT: {left}")
                        else:
                            dq.pop()
                            result.append(right)
                            moves.append('R')
                            print(f"  Both continue, chose larger RIGHT: {right}")
                else:
                    dq.pop()
                    result.append(right)
                    moves.append('R')
                    print(f"  No pattern -> chose RIGHT: {right}")
            else:
                dq.pop()
                result.append(right)
                moves.append('R')
                print(f"  Early stage -> chose RIGHT: {right}")
        
        if step > 10:
            break
    
    print(f"\nFinal result: {result}")
    print(f"Final moves: {''.join(moves)}")
    print(f"Expected: RRRLLLL")
    return ''.join(moves)

# Test case 1
p1 = [1, 2, 3, 4, 5, 6, 7]
solve_debug_detailed(p1)
