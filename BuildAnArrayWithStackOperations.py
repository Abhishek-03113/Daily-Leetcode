"""
@Abhishek 
Day 22 : Daily Challenge 

Topic : Stack and Array
"""

class Solution: 
    def buildArray(self,target,n):

        ans = []

        prev = 1

        for x in target: 

            while prev != target:

                ans.append("PUSH")
                ans.append("POP")

                prev += 1

            ans.append("PUSH")

            prev += 1



        return ans
        
        # Optimized Solution using stack 


        ans = []

        prev = 1

        for x in target: 

            while prev != target:

                ans.append("PUSH")
                ans.append("POP")

                prev += 1

            ans.append("PUSH")


            return ans









