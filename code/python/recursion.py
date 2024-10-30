# def count(child_dict, i):
#     if i not in child_dict.keys():
#         return 1
#     ans = 1
#     for j in child_dict[i]:
#         ans += count(child_dict, j)
#     return ans

# child_dict = dict()
# child_dict[0] = [1, 2]
# child_dict[1] = [3, 4, 5]
# child_dict[2] = [6, 7, 8]

# print(child_dict.keys())
# # print(count(child_dict, 0))
# # class Solution:
# #     def subArraySum(self, arr, n, s): 
# #         # Write your code here

# #         final = sum(arr)
        
# #         l, r = 0, n - 1
        
# #         while l <= r:
# #             if final > s:
# #                 if arr[l] > arr[r]:
# #                     final -= arr[l]
# #                     l += 1
# #                 else:
# #                     final -= arr[r]
# #                     r -= 1
# #             elif final < s:
# #                 if arr[l] < arr[r]:
# #                     final -= arr[l]
# #                     l += 1
# #                 else:
# #                     final -= arr[r]
# #                     r -= 1
# #             else:
# #                 return [l + 1, r + 1]  # Return 1-based index as per common convention
        
# #         return [-1]  # Return -1 if no subarray is found
# # # import math

# # # def subsets(ind, ds, arr):
    
# # #     if ind == len(arr):
# # #         print(ds)
# # #         return 
    
    
# # #     subsets(ind + 1, ds, arr) 
# # #     ds.append(arr[ind]) 
# # #     subsets(ind + 1, ds, arr)
# # #     ds.pop()

# # # def iterative(arr, n):
    
# # #     ds = [] 
# # #     j = 0
# # #     for j in range(0, j << n):
        
# # #         for i in range(n): 
            
# # #             if arr[i] and 1<<i: 
# # #                 ds.append(i)  
        
# # #         print(ds)
            
    


# # # arr = [3,1,2] 
# # # ds = []
# # # # subsets(0, ds, arr) 

# # # iterative(arr, len(arr)) 


