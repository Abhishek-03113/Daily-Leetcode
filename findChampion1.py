"""
@Abhishek 
Day 24
Topic : 2D matrix, array 

First Contenst Problem 

"""


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        winner = 0

        countstrong = {}

        n = len(grid[0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if i not in countstrong:
                        countstrong[i] = 1
                    else:
                        countstrong[i] += 1

        win = max(countstrong.values())

        for i in countstrong:
            if countstrong[i] == win:
                winner = i

        return winner
