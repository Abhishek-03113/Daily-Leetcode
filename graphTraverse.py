"""
@Abhishek 
Day 30 : Daily Challenge 
Topic : Graph 

"""


class Graph:

    """Approach 1 : Dijkstra's Algorithm"""

    # def __init__(self, n: int, edges: List[List[int]]):
    #     self.adj_list = [[] for _ in range(n)]
    #     for from_node, to_node, cost in edges:
    #         self.adj_list[from_node].append((to_node, cost))

    # def addEdge(self, edge: List[int]) -> None:
    #     from_node, to_node, cost = edge
    #     self.adj_list[from_node].append((to_node, cost))

    # def shortestPath(self, node1: int, node2: int) -> int:
    #     n = len(self.adj_list)
    #     pq = [(0, node1)]
    #     cost_for_node = [inf] * (n)
    #     cost_for_node[node1] = 0

    #     while pq:
    #         curr_cost, curr_node = heappop(pq)
    #         if curr_cost > cost_for_node[curr_node]:
    #             continue
    #         if curr_node == node2:
    #             return curr_cost
    #         for neighbor, cost in self.adj_list[curr_node]:
    #             new_cost = curr_cost + cost
    #             if new_cost < cost_for_node[neighbor]:
    #                 cost_for_node[neighbor] = new_cost
    #                 heappush(pq, (new_cost, neighbor))
    #     return -1

    """ Approach 2 : Floyyed Warshal's Algorithm """

    def __init__(self, n, edges):
        self.adj_matrix = [[inf] * n for _ in range(n)]
        for from_node, to_node, cost in edges:
            self.adj_matrix[from_node][to_node] = cost
        for i in range(n):
            self.adj_matrix[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.adj_matrix[j][k] = min(
                        self.adj_matrix[j][k],
                        self.adj_matrix[j][i] + self.adj_matrix[i][k],
                    )

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        n = len(self.adj_matrix)
        for i in range(n):
            for j in range(n):
                self.adj_matrix[i][j] = min(
                    self.adj_matrix[i][j],
                    self.adj_matrix[i][from_node] + self.adj_matrix[to_node][j] + cost,
                )

    def shortestPath(self, node1, node2):
        if self.adj_matrix[node1][node2] == inf:
            return -1
        return self.adj_matrix[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
