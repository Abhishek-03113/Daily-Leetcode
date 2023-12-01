"""
@Abhishek 
Day 26 : Daily Challenge 

Topic : array,  sorting  
"""


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # n monsters
        # dist : distance in km of ith monster
        # speed : speed of  monsters
        #

        """Approach 1 : sorted arrival time"""
        # count = 0
        # arrival = []
        n = len(dist)
        # for i in range(n):
        #     arrival.append(dist[i]/speed[i])

        # arrival.sort()

        # for i in range(len(arrival)):
        #     if arrival[i] <= i:
        #         break
        #     count += 1

        # return count

        """Approach 2 : Heap """

        heap = []

        for i in range(n):
            heap.append((dist[i] / speed[i]))

        heapq.heapify(heap)

        ans = 0

        while heap:
            if heapq.heappop(heap) <= ans:
                break

            ans += 1

        return ans
