import sys
 
# Utility function for solving the minimum coins problem
 
def minCoinsUtil(coins, m, V, dp):
    # Base case: If target value V is 0, no coins are needed
    if V == 0:
        return 0
 
    # If subproblem is already solved, return the result from DP table
    if dp[V] != -1:
        return dp[V]
 
    res = sys.maxsize
 
    # Iterate over all coins and recursively solve for subproblems
    for i in range(m):
        if coins[i] <= V:
            # Recursive call to solve for remaining value V - coins[i]
            sub_res = minCoinsUtil(coins, m, V - coins[i], dp)
 
            # If the subproblem has a valid solution and the total number of coins
            # is smaller than the current result, update the result
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
 
    # Save the result in the DP table
    dp[V] = res
 
    return res
 
# Function to find the minimum number of coins needed to make a target value
 
 
def minCoins(coins, m, V):
    # Create a DP table to store results of subproblems
    dp = [-1] * (V + 1)
    # Call the utility function to solve the problem
    return minCoinsUtil(coins, m, V, dp)
 
 
# Driver code
if __name__ == "__main__":
    t = int(input()) 
    for _ in range(t): 
        coins = [1, 3, 6, 10,15]
        m = len(coins)
        V = int(input())
        res = minCoins(coins, m, V)
    
        if res == sys.maxsize:
            res = -1
        # Find the minimum number of coins required
        print("Minimum coins required is", res)