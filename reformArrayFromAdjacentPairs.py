"""
@Abhishek 
Day 29 Daily Challenge 
Topic Graph Traversal 

"""


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)

        root = None

        for i in graph:
            if len(graph[i]) == 1:
                root = i
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for i in graph[node]:
                if i != prev:
                    dfs(i, node, ans)

        ans = []
        dfs(root, None, ans)

        return ans
