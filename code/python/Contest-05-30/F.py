class Solution:
    def threeSumClosest(self, nums, target) :
        nums.sort() 
        n = len(nums) 
        ans = 0 
        diff = float('inf')

        print(nums)
        for i in range(n):
            l, r = i+1, n - 1 
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                df = abs(sm - target)
                
                print(nums[i], nums[l], nums[r], sm, df) 

                if df == 0:
                    return sm
                
                # print(sm, df, diff)

                if df < diff:
                    ans = sm
                    diff = df 


                if sm < target:
                    l += 1
                
                elif sm >= target:
                    r -= 1 
            


        return ans

ck
nums = [4,0,5,-5,3,3,0,-4,-5] 

target = -2 

sol = Solution() 
print(sol.threeSumClosest(nums, target)) # Expected  -2
