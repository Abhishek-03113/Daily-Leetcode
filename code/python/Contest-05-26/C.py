for _ in range(int(input())):
    
    N = int(input()) 
    
    S = input() 
    
    total_sum = 0
    for L in range(N):
        freq = {'0': 0, '1': 0}
        for R in range(L, N):
            freq[S[R]] += 1
            
            max_freq = max(freq.values())
            modes_count = list(freq.values()).count(max_freq)
            total_sum += modes_count
            
    print(total_sum) 
    
        

    
    # zeros = [0] * (N + 1)
    # ones = [0] * (N + 1)

    # for i in range(N):
    #     zeros[i + 1] = zeros[i] + (1 if S[i] == '0' else 0)
    #     ones[i + 1] = ones[i] + (1 if S[i] == '1' else 0)
    
    # ans = 0
    
    # # Evaluate all substrings
    # for L in range(N):
    #     for R in range(L, N):
    #         count_0 = zeros[R + 1] - zeros[L]
    #         count_1 = ones[R + 1] - ones[L]
            
    #         if count_0 > count_1:
    #             ans += 1
    #         elif count_1 > count_0:
    #             ans += 1
    #         else:
    #             ans += 2
                
    # print(ans)