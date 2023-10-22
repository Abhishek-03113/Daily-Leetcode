"""
@Abhishek 
N Queen Problem using CSP and BackTracking 

"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for prev_row in range(row):
                if board[prev_row][col] == "Q":
                    return False
                if (
                    col - (row - prev_row) >= 0
                    and board[prev_row][col - (row - prev_row)] == "Q"
                ):
                    return False
                if (
                    col + (row - prev_row) < n
                    and board[prev_row][col + (row - prev_row)] == "Q"
                ):
                    return False
            return True

        def backtrack(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(0)
        return solutions
