#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        a = [0] * n 
        
        visited = set() 
        
        for i in range(1,n):
            a[i] = a[i-1] - i
            
            if a[i] <= 0 or a[i] in visited : 
                a[i] = a[i-1] + i 
            
            visited.add(a[i]) 
        
        
        return a 
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
