def max_xor_sum(arr):
    """
    Find the maximum value of (ak⊕a1) + (ak⊕a2) + ... + (ak⊕an) among all 1≤k≤n.
    
    Args:
        arr: A list of integers representing the array [a1, a2, ..., an]
    
    Returns:
        A tuple (max_sum, k) where max_sum is the maximum sum and k is the index (1-indexed)
    """
    n = len(arr)
    max_sum = float('-inf')
    max_k = 0
    
    # Try each possible k
    for k in range(n):
        # Calculate the sum for this k
        current_sum = 0
        for i in range(n):
            # Calculate ak ⊕ ai and add to sum
            # Note: k and i are 0-indexed, but the problem uses 1-indexed
            current_sum += arr[k] ^ arr[i]
        
        # Update maximum if needed
        if current_sum > max_sum:
            max_sum = current_sum
            max_k = k + 1  # Convert to 1-indexed
    
    return max_sum, max_k

# Example usage
def main():
    # Example array
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    
    max_sum, k = max_xor_sum(arr)
    print(f"Maximum sum: {max_sum}")
    print(f"Achieved with k = {k} (a{k} = {arr[k-1]})")

if __name__ == "__main__":
    main()