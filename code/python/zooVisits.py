import sys
sys.setrecursionlimit(10000)  

def help():
    N, M = map(int, input().split())
    fees = list(map(int, input().split()))
    
    
    animal = []
    for i in range(M):
        entry = list(map(int, input().split()))
        K = entry[0]
        zoos = [z-1 for z in entry[1:]]  
        animal.append(zoos)
    
    
    bit_mask = [0] * N
    for animal_idx, zoos in enumerate(animal):
        for zoo in zoos:
            bit_mask[zoo] |= (1 << animal_idx)
    
    
    
    full_mask = (1 << (2*M)) - 1
    
    
    INF = float('inf')
    memo = {}
    
    def solve(mask):
        
        if mask == 0:
            return 0
            
        
        if mask in memo:
            return memo[mask]
        
        result = INF
        
        for zoo in range(N):
            zoo_animals = bit_mask[zoo]
            
            
            new_mask = mask
            for animal in range(M):
                if (zoo_animals & (1 << animal)) > 0:
                    
                    needs_two = (new_mask & (1 << (M + animal))) > 0
                    needs_one = (new_mask & (1 << animal)) > 0
                    
                    if needs_two:
                        
                        new_mask &= ~(1 << (M + animal))
                        new_mask |= (1 << animal)
                    elif needs_one:
                        
                        new_mask &= ~(1 << animal)
            
            
            if new_mask != mask:
                result = min(result, solve(new_mask) + fees[zoo])
        
        memo[mask] = result
        return result
    
    
    
    
    
    initial_mask = 0
    for i in range(M):
        initial_mask |= (1 << i)  
        initial_mask |= (1 << (M + i))  
    
    return solve(initial_mask)

print(help())