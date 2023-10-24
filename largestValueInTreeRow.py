"""
@Abhishek 
Day 13 
Topic : Trees 

"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            curr_level_size = len(queue)
            max_val = float("-inf")

            for _ in range(curr_level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            result.append(max_val)

        return result
