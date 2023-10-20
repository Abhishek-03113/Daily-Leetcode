"""
@Abhishek 
Day 5 : Problem 1 
I believe we can solve this problem using stack 
Hope I can do it without looking at the solution

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False

        stack = []

        for i in range(len(s)):
            if  s[i] =='(' or s[i] == '[' or s[i] == '{' : stack.append(s[i])


            if s[i] ==')' or s[i] == ']' or s[i] == '}' :
                if len(stack) == 0:
                    return False
                try:
                    ch = stack.pop(-1)
                    if (s[i] ==')' and ch !="(") or (s[i]=="]" and ch!="[") or (s[i]=='}' and ch != "{"):
                        return False
                except:
                    continue

            
            
        return len(stack) == 0


        