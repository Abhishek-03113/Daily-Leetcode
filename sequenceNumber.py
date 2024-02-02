class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        a = [] 

        for i in range(1, 10): 

            num = i 

            next_dig = i + 1
             
            while num <= high and next_dig <= 9: 
                num = num * 10 + next_dig

                if low <= num <= high: 
                    a.append(num)

                next_dig += 1 

        a.sort() 

        return a 
        
