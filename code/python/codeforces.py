def solve_test_case(N, K, A):

    freq = {}
    k_positions = {}

    for i, num in enumerate(A):
        freq[num] = freq.get(num, 0) + 1
        if num == K:
            k_positions[i] = True 

    k_freq = freq.get(K, 0)
    mx = max((freq[x] for x in freq if x != K), default=0)
    
    if len(A) > 2:
        if k_freq > mx:
            return 0

        if k_positions.get(0, -1) != -1 or k_positions.get(N-1, -1) != -1:
            return 1 

        elif k_positions.get(1, -1) != -1 or k_positions.get(N-2, -1) != -1: 
            return 1 
        
        else: 
            return 2  
    else: 
        return 0 
    
    

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        result = solve_test_case(N, K, A)
        print(result)


if __name__ == "__main__":
    main()
