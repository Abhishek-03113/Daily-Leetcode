def solve():
    n = int(input())
    b = list(map(int, input().split()))
    
    # Simple greedy simulation with debug output
    curr = [0] * n
    for step in range(sum(b) + 100):
        if curr == b:
            print("YES")
            return
        min_val = min(curr)
        found = False
        
        for x in range(min_val + 1, min_val + 101):
            leftmost = -1
            for i in range(n):
                if curr[i] < x:
                    leftmost = i
                    break
            
            if leftmost != -1 and curr[leftmost] + x <= b[leftmost]:
                old_curr = curr[:]
                curr[leftmost] += x
                print(f"Step {step}: x={x}, leftmost={leftmost}, {old_curr} -> {curr}")
                found = True
                break
        
        if not found:
            print(f"No valid move found at step {step}, curr={curr}, target={b}")
            print("NO")
            return
    print("NO")

for _ in range(int(input())):
    solve()
