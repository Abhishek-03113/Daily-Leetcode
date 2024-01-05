

class Solution:

	def TotalWays(self, N):

		# Code here

		

		MOD = 10**9 + 7 

		

		x,y = 1, 2 

		

		for i in range(2, N+1):

		    

		    z = y 

		    z += x 

		    

		    z %= MOD 

		    

		    x,y = y, z

	    

	    return (y**2) % MOD
