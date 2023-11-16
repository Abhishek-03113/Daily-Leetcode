"""
@Abhishek 
Day 35 : Daily Challenge 
Topic : String, Array
"""

## Given : array of strings  nums : n unique binary strings of length n
## Output : a binary string of length n that is not in nums 
## if multiple answers we can return any of them 


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums = set(nums) 
        # def generate(curr):
        #     if len(curr) == n:
        #         if curr not in nums:
        #             return curr 
        #         return ""
            
        #     add_zero = generate(curr+"0")
        #     if add_zero:
        #         return add_zero 
        #     return generate(curr + "1") 
         
        # n = len(nums) 

        # return generate("")

        # ans = []
        # for i in range(len(nums)):
        #     curr = nums[i][i]
        #     ans.append("1" if curr == "0" else "0")
        
        # return "".join(ans)

        # integers = set()
        # for num in nums:
        #     integers.add(int(num, 2))

        # n = len(nums)
        # for num in range(n + 1):
        #     if num not in integers:
        #         ans = bin(num)[2:]
        #         return "0" * (n - len(ans)) + ans
            
        # return ""

        # integers = set()
        # for num in nums:
        #     integers.add(int(num, 2))

        # ans = int(nums[0], 2)
        # n = len(nums)

        # while ans in integers:
        #     ans = random.randrange(0, 2 ** n)
        
        # s = bin(ans)[2:]
        # return "0" * (n - len(s)) + s
