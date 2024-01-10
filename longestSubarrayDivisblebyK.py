class Solution:

	def longSubarrWthSumDivByK (self,arr,  n, k) : 

		#Complete the function

		

		# arr of size N and a value K 

		# find : longest sub array with sum of elements divisble by values of K 

		

		total, ans = 0, 0 

		

		mp = dict() 

		

		for i in range(n):

		    

		    total += arr[i]

		    

		    rem = total % k 

		    

		    if rem == 0: 

		        ans = max(ans, i+1)

		    

		    if rem not in mp: 

		        mp[rem] = i 

		       

		    else:

		        ans = max(ans, i - mp[rem])

		 

        return ans 
