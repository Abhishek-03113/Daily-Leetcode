class Solution:

    

    #Function to check if a string is Pangram or not.

    def checkPangram(self,s):

        lower_s = s.lower()

        letters = [chr(a) for a in range(97, 97+26)]

        return all([(l in lower_s) for l in letters])





        

        
