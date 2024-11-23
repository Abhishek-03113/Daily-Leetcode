def spiccy():
    
    n, k = map(int, input().split()) 
    a = list(map(int, input().split())) 
    a.sort() 
    
    pre = [0] * (n)
    pre[0] = a[0]
    for i in range(1, n): 
        pre[i] = pre[i - 1] + a[i]
    
    ans = [0]*(n)
    ans[0] = pre[0] 
    new = [0]*n 
    new[0] = a[0]
  
    
    if k == 1:
        for i in range(1, n): 
        
            if i < k: 
                new[i] = new[i-1] + a[i] 
                ans[i] = new[i] 
            else: 
                new[i] = a[i] + new[i-2] 
                ans[i] = new[i] 

        
    else: 
        for i in range(1, n):
            
            if i < k:
                ans[i] = pre[i] 
            else: 
                ans[i] = pre[i] - pre[i-k] +  pre[i-k-1] if i-k-1 >= 0 else pre[i] - pre[i-k] 
            
    print(ans)
        
            
for _ in range(int(input())): 
    spiccy() 


# def solve(n):
#     MOD = 998244353
    
#     def get_binary(x):
#         return bin(x)[2:]  # Remove '0b' prefix
    
#     # For processing large numbers modularly
#     def process_string_modulo(s):
#         result = 0
#         for digit in s:
#             # For each digit, multiply current result by 10 and add digit
#             result = (result * 10 + int(digit)) % MOD
#         return result
    
#     # Build the binary string incrementally with modular arithmetic
#     final_str = ""
#     curr_len = 0
    
#     # Process numbers from 1 to n
#     for i in range(1, n + 1):
#         binary = get_binary(i)
#         # If string gets too long, process it modularly
#         if curr_len > 1000000:  # Arbitrary large threshold
#             final_str = str(process_string_modulo(final_str))
#             curr_len = len(final_str)
#         final_str += binary
#         curr_len += len(binary)
    
#     return process_string_modulo(final_str)

# # Read input
# t = int(input())
# numbers = list(map(int, input().split()))

# # Process each test case
# for n in numbers:
#     print(solve(n))

# def calculate_edge_cost(i, j, positions, costs):
#     """Calculate the cost of connecting points i and j"""
#     return min(costs[i], costs[j]) * abs(positions[i] - positions[j])

# def find_parent(parent, x):
#     """Find parent with path compression"""
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union(parent, rank, x, y):
#     """Union by rank"""
#     px, py = find_parent(parent, x), find_parent(parent, y)
#     if rank[px] < rank[py]:
#         px, py = py, px
#     parent[py] = px
#     if rank[px] == rank[py]:
#         rank[px] += 1

# def solve_testcase(n, positions, costs):
#     # Create edges with their costs
#     edges = []
#     for i in range(n):
#         for j in range(i + 1, n):
#             cost = calculate_edge_cost(i, j, positions, costs)
#             edges.append((cost, i, j))
    
#     # Sort edges by cost
#     edges.sort()
    
#     # Initialize union-find data structures
#     parent = list(range(n))
#     rank = [0] * n
    
#     # Kruskal's algorithm
#     total_cost = 0
#     edges_used = 0
    
#     for cost, u, v in edges:
#         if find_parent(parent, u) != find_parent(parent, v):
#             union(parent, rank, u, v)
#             total_cost += cost
#             edges_used += 1
#             if edges_used == n - 1:
#                 break
    
#     return total_cost

# def main():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         positions = list(map(int, input().split()))
#         costs = list(map(int, input().split()))
#         result = solve_testcase(n, positions, costs)
#         print(result)

# if __name__ == "__main__":
#     main()