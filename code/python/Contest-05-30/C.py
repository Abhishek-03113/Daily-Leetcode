from typing import List
from collections import deque

def count_regions(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    regions = 0

    def bfs(i: int, j: int):
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not visited[i][j]:
                bfs(i, j)
                regions += 1
    return regions

def solve(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    initial_regions = count_regions(grid)
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1
                new_regions = count_regions(grid)
                if new_regions == 3:
                    count += 1
                grid[i][j] = 0
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = []
        for _ in range(2):
            row = [0 if c == '.' else 1 for c in input()]
            grid.append(row)
        print(solve(grid))

if __name__ == "__main__":
    main()