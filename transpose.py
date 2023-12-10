class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:


        row = len(matrix)
        col = len(matrix[0])

        ans = [[None]*row for _ in range(col)]

        for r, ro in enumerate(matrix):

            for c, co in enumerate(ro):
                ans[c][r] = co 
        
        return ans 
