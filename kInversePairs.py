class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        mod = 10**9 + 7  # Define the modulus value to keep numbers within integer bounds
      
        # dp table representing the count of inverse pairs for the current number of integers
        dp = [1] + [0] * k  
      
        # Prefix sum array for optimization of the inner loop. The size is k+2 for 1-indexed and ease of access
        prefix_sum = [0] * (k + 2)
      
        # Iterate through integers from 1 to n
        for current_number in range(1, n + 1):
            # Going through all possible counts of inverse pairs from 1 to k
            for inverse_count in range(1, k + 1):
                # Update the dp table by taking the count from the prefix_sum within the range
                # The range corresponds to the valid inverse pair counts that can be formed with the current number
                dp[inverse_count] = (prefix_sum[inverse_count + 1] - 
                                     prefix_sum[max(0, inverse_count - (current_number - 1))]) % mod
          
            # Updating prefix_sum based on the updated dp table
            for index in range(1, k + 2):
                prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod
              
        # Returning the number of ways to form k inverse pairs with n integers
        return dp[k]
