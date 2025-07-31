def analyze_expected():
    """Analyze what the expected outputs actually do"""
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], "RRRLLLL"),
        ([1, 3, 6, 8, 9, 7, 5, 4, 2], "LLRRLLRRL"),
        ([1, 2, 11, 3, 6, 4, 7, 8, 12, 5, 10, 9], "LLLLLLLLLLLL"),
        ([4, 1, 2, 5, 6, 3], "LLLLLL"),
        ([1, 2, 3, 5, 4], "LLLLL"),
        ([5, 1, 8, 6, 2, 7, 9, 4, 3], "LLLLLLLLL")
    ]
    
    for i, (p, expected) in enumerate(test_cases):
        print(f"\nTest case {i+1}: {p}")
        print(f"Expected moves: {expected}")
        
        from collections import deque
        dq = deque(p)
        result = []
        
        for move in expected:
            if move == 'L':
                val = dq.popleft()
            else:
                val = dq.pop()
            result.append(val)
        
        print(f"Result: {result}")
        
        # Check for patterns
        count_R = expected.count('R')
        count_L = expected.count('L')
        print(f"R count: {count_R}, L count: {count_L}")
        
        # Find switch points
        switch_points = []
        current = expected[0]
        for j, move in enumerate(expected[1:], 1):
            if move != current:
                switch_points.append(j)
                current = move
        print(f"Switch points: {switch_points}")

analyze_expected()
