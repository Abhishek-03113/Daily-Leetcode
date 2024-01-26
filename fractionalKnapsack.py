

class Item:

    def __init__(self,val,w):

        self.value = val

        self.weight = w

        

class Solution:    

    #Function to get the maximum total value in the knapsack.

    def fractionalknapsack(self, W,arr,n):

        

       

        capacity=0

        answer=0

        arr.sort(key=lambda x:x.value / x.weight , reverse = True)

        

        for item in arr:

            if capacity + item.weight <= W:

                capacity += item.weight

                answer += item.value

                

            elif capacity == W:

                break

            

            else:

                remain= W - capacity 

                answer += remain * ( item.value / item.weight )

                capacity+= remain

                

        return answer 
