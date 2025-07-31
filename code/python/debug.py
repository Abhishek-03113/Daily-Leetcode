import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7

def io():
    return map(int, input().split())

def iol():
    return list(map(int, input().split()))

def ios():
    return input().strip()

def ioi():
    return int(input().strip())

def iom(n, m):
    return [list(map(int, input().split())) for _ in range(n)]

def solve():
    n = ioi()
    b = iol()
    
    def can_construct():
        curr = [0] * n
        
        # Generate comprehensive candidate x values
        candidates = set()
        
        # Add all values from 1 to a reasonable limit
        for i in range(1, min(50, max(b) + 1)):
            candidates.add(i)
            
        # Add target values and their factors
        for val in b:
            candidates.add(val)
            for div in range(1, min(8, val + 1)):
                if val % div == 0:
                    candidates.add(val // div)
                candidates.add(div)
        
        candidates = sorted(list(candidates))
        print(f"Candidates: {candidates[:20]}...")  # Debug
        
        # Simulate construction
        max_ops = min(500, sum(b) * 3)
        
        for op in range(max_ops):
            if curr == b:
                print(f"Success after {op} operations!")
                return True
                
            min_val = min(curr)
            progress_made = False
            
            # Try each candidate x value
            for x in candidates:
                if x <= min_val:
                    continue
                    
                # Find leftmost position with curr[i] < x
                leftmost_idx = -1
                for i in range(n):
                    if curr[i] < x:
                        leftmost_idx = i
                        break
                
                if leftmost_idx == -1:
                    continue
                
                # Allow any move that doesn't exceed target
                if curr[leftmost_idx] + x <= b[leftmost_idx]:
                    old_curr = curr[:]
                    curr[leftmost_idx] += x
                    print(f"Op {op}: x={x}, leftmost={leftmost_idx}, {old_curr} -> {curr}")
                    progress_made = True
                    break
            
            if not progress_made:
                print(f"No progress at operation {op}, curr={curr}, target={b}")
                return False
        
        print(f"Reached max operations, curr={curr}, target={b}")
        return curr == b
    
    result = can_construct()
    print("YES" if result else "NO")

for _ in range(int(input())):
    solve()
