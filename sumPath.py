'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def help(self,root,sum,l,ans):
        if root:
            sum-=root.data
            l.append(root.data)
            if sum==0:
                ans.append(l.copy())
            self.help(root.left,sum,l,ans)
            self.help(root.right,sum,l,ans)
            l.pop()

    def printPaths(self, root, sum):
        ans=[]
        l=[]
        self.help(root,sum,l,ans)
        return ans
     #code here
