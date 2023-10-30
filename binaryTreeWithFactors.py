"""
@Abhishek 
Day 16 
Topic : Binary Trees, Dynamic Programming 
"""


class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Sort the input array in ascending order
        arr.sort()
        # Create a dictionary to store intermediate results
        dp = {}

        # Iterate through each number in the sorted array
        for i in arr:
            # Initialize the number of binary trees with just the current number as 1
            dp[i] = 1

            # Iterate through the array again
            for j in arr:
                # Check if 'i' is divisible by 'j' and if the result of the division is already in the dictionary
                if i % j == 0 and i // j in dp:
                    # Update the number of binary trees for 'i' by multiplying the counts of 'j' and 'i//j'
                    dp[i] += dp[j] * dp[i // j]

        # Initialize the final result
        result = 0
        # Sum up all the values in the 'dp' dictionary
        for val in dp.values():
            result += val

        # Return the result as an integer after applying the modulo operation
        return int(result % (10**9 + 7))
