"""
@Abhishek 
Day 23 : Daily Problem 

Topic : Array, simulation 

"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        wooden plank of n length

        ants walking on that plank

        ant speed = 1 unit/s

        some ants moving right and some left

        when two ants meet at some points they change their direction

        when ant reachers the end of plank at time t, it falls out of plank

        given :
        integer n,
        two integer arrays : left and right : positions of ants moving left and right,

        to find :

        return the last moment when last ant fall out of plank
        """

        ans = 0

        for i in left:
            ans = max(ans, i)

        for j in right:
            ans = max(ans, n - j)

        return ans
