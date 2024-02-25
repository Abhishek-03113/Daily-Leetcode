class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp = [0] * (n + 1)

        # There is one way to achieve a score of 0 (no moves)
        dp[0] = 1

        # Iterate through each move (3, 5, 10)
        for move in [3, 5, 10]:
            # Update dp array for each score from move to n
            for score in range(move, n + 1):
                dp[score] += dp[score - move]

        return dp[n]

