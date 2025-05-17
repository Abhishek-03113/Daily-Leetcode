class Solution: 
    def minPathSum(self, grid):
        
        ans = 0 
        
        visited = set() 
        
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                dp[i][j] = grid[i][j] 
                
                if i > 0 and j > 0: 
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]
                
        return dp[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
sol = Solution()

print(sol.minPathSum(grid))