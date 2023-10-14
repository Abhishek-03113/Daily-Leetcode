"""
@Abhishek Day4 : problem 2 
solved completely by myself
not very optimized


"""


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """ 

        n = len(s)

        position = []
        answer = [1 for i in range(len(s))]

        for i in range(n):
            if s[i] == c:
                position.append(i)
                answer[i] = 0
    


        for i in range(n):
            temp = [abs(data-i) for data in position]
            if answer[i] == 0:
                continue
            else:
                answer[i] = min(temp)


        
        return answer
            


            

            


            

        
