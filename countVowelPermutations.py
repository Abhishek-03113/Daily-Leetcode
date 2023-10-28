"""
@Abhishek 
Day 18 
LeetCode Daily 

"""


class Solution:
    M = 1_000_000_007

    def countVowelPermutation(self, n: int) -> int:
        # Initialize a count matrix with one row representing the counts of 'a', 'e', 'i', 'o', and 'u'.
        count = [[1, 1, 1, 1, 1]]
        finalMatrix = []

        # If n is greater than 1, perform matrix operations to calculate the count.
        if n > 1:
            # Define the base transition matrix that represents the vowel transitions.
            base = [
                [0, 1, 1, 0, 1],
                [1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0],
            ]

            # Calculate the final matrix by raising the base matrix to the power (n - 1).
            finalMatrix = self.matrixMul(count, self.matrixPow(base, n - 1))
        else:
            finalMatrix = (
                count  # If n is 1, the result is the same as the initial count matrix.
            )

        # Calculate the result by summing up the values in the finalMatrix and taking the modulo M.
        result = 0
        for l in finalMatrix[0]:
            result += l
        result %= self.M
        return int(result)

    # Function to calculate the matrix raised to a power using a recursive approach.
    def matrixPow(self, base, pow):
        if pow == 1:
            return base
        if pow == 2:
            return self.matrixMul(base, base)
        matrixPow = self.matrixPow(base, pow // 2)
        matrix = self.matrixMul(matrixPow, matrixPow)
        if pow % 2 == 0:
            return matrix
        else:
            return self.matrixMul(matrix, base)

    # Function to perform matrix multiplication.
    def matrixMul(self, a, b):
        ai = len(a)
        bi = len(b)
        bj = len(b[0])
        result = [[0 for _ in range(bj)] for _ in range(ai)]
        for i in range(ai):
            for j in range(bj):
                sum = 0
                for k in range(bi):
                    sum += a[i][k] * b[k][j]
                    sum %= self.M
                result[i][j] = sum
        return result
