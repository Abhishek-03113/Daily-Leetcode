"""
@Abhishek 
Day 7: Problem 1 

"""

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        """
        n binary tree nodes 0 - (n-1)

        """
        graph = defaultdict(list)
        in_degree = [0] * n

        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                graph[node].append(left)
                in_degree[left] += 1
            if right != -1:
                graph[node].append(right)
                in_degree[right] += 1

        root_candidates = [node for node in range(n) if in_degree[node] == 0]

        if len(root_candidates) != 1:
            return False  
        root = root_candidates[0]

        queue = [root]
        seen = set([root])

        while queue:
            node = queue.pop(0)
            if node in graph:
                for child in graph[node]:
                    if child in seen:
                        return False  
                    seen.add(child)
                    queue.append(child)

        return len(seen) == n

