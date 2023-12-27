class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            d = 0
            for j in range(n):
                if grid[i][j] == 1:
                    d += 1
                else:
                    d -= 1
            for j in range(n):
                diff[i][j] += d
        for j in range(n):
            d = 0
            for i in range(m):
                if grid[i][j] == 1:
                    d += 1
                else:
                    d -= 1
            for i in range(m):
                diff[i][j] += d

        return diff

        
