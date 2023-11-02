"""
@Abhishek 
Day 21 : Daily Problem  
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ## Approach : Dept First Search

        ans = 0

        def dfs(root):
            nonlocal ans

            if not root:
                return [0, 0]

            leftsum, leftcount = dfs(root.left)
            rightsum, rightCount = dfs(root.right)

            nodeSum = leftsum + rightsum + root.val

            nodeCount = leftcount + rightCount + 1

            if nodeSum // nodeCount == root.val:
                ans += 1

            return [nodeSum, nodeCount]

        dfs(root)

        return ans
