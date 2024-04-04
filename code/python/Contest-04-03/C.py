def queue_simulation(n, patience_levels):
    queue_size = [0] * (n + 1)  # Initialize array to store queue sizes

    for patience in patience_levels:
        # Update queue size for each second
        for i in range(1, n + 1):
            if patience >= i:
                queue_size[i] += 1 # Increment queue size if person hasn't left yet
            else:
                break  # Exit loop if person's patience level is exceeded

    return queue_size[1:]  # Exclude the initial 0 from the result

# Test case
t = int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input())
    patience_levels = list(map(int, input().split()))
    result = queue_simulation(n, patience_levels)
    print(" ".join(map(str, result)))
