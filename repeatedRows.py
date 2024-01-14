class Solution:
    def repeatedRows(self, arr, m ,n):
        s = []
        ans = []
        
        for i in range(len(arr)):
            
            if arr[i] not in s:
                s.append(arr[i])
            
            else:
                ans.append(i)
            
                
        # print(s)
        
        return ans
        
