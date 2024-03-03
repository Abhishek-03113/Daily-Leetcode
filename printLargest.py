from functools import cmp_to_key



class Solution:



	def printLargest(self, n, arr):

	    def compare(x,y):

            xy=x+y

            yx=y+x

            if xy<yx:

                return 1

            elif xy>yx:

                return -1

            else:

                return 0

        a=""

        arr.sort(key=cmp_to_key(compare))

        for i in range(n):

            a+=arr[i]

        return a

	    # code here

