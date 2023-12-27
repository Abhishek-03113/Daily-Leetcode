class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        # given an mxn matrix # return number of special positions 
        # in special position mat[i][j] == 1 and all other row and column elements are 0
        
        # r = len(mat) 
        # c = len(mat[0]) 
        # ans = 0 


        # for row in range(r):

        #     for col in range(c):

        #         if mat[row][col] == 0: 
        #             continue 
        #         good = True 


        #         for i in range(r):

        #             if i != row and mat[i][col] == 1:
        #                 good = False
        #                 break 
                
        #         for j in range(c):

        #             if j != col and mat[row][j] == 1:
        #                 good = False
        #                 break 
                
        #         if good:
        #             ans += 1

        # return ans

        return sum(
            sum(mat[i][col] for i in range(len(mat))) == 1
            for col in [
                row.index(1)
                for row in mat
                if sum(row) == 1
            ]
        )

    
