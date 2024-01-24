class Solution:

    def isTree(self, n, m, edges):

        adj_list = {i: [] for i in range(n)}



        for edge in edges:

            u, v = edge

            adj_list[u].append(v)

            adj_list[v].append(u)



        # Create a set to keep track of visited nodes during DFS

        visited = set()



        # Helper function to perform DFS

        def dfs(node, parent):

            # If the node is already visited, the graph has a cycle

            if node in visited:

                return False



            visited.add(node)



            # Visit neighbors of the current node

            for neighbor in adj_list[node]:

                # Skip the parent, as it is already visited in the previous step

                if neighbor != parent:

                    if not dfs(neighbor, node):

                        return False



            return True



        # Check if the graph is connected and has no cycles

        if not dfs(0, -1) or len(visited) != n:

            return 0



        # If the graph is connected and has no cycles, it is a tree

        return 1
