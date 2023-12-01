"""
@Abhishek 
day 31
"""


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        """Approach 1: Breadth-First Search (BFS) with Bus Stops as Nodes"""
        if target == source:
            return 0
        adj_list = defaultdict(set)
        for group, route in enumerate(routes):
            for stop in route:
                adj_list[stop].add(group)
        queue = [(source, 0)]
        visited = set()
        buses = 1
        for stop, buses in queue:
            if stop == target:
                return buses
            for group in adj_list[stop]:
                for nei in routes[group]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, buses + 1))
                routes[group] = []
        return -1
