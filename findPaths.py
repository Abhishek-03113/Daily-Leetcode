class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        in_range = lambda x, y: 0 <= x < m and 0 <= y < n
        @cache
        def go(i, j, moves):
            if not in_range(i, j):
                return 1
            if moves == 0:
                return 0
            res = 0
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                i1 = i + di
                j1 = j + dj
                res += go(i1, j1, moves-1)
                res %= MOD
            return res
        
        return go(startRow, startColumn, maxMove)
