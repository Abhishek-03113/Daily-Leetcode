class Solution:
    def resolves(self, a, b, op): 
        if op == '+': 
            return a + b 
        
        elif op == '-':
            return a-b 
        
        elif op == '*': 
            return a * b 
        
        return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 

        for token in tokens: 

            if len(token) == 1 and ord(token) < 48: 
                int2 = stack.pop() 
                int1 = stack.pop() 

                op = token

                res = self.resolves(int1, int2, op) 

                stack.append(res) 

            else:
                stack.append(int(token)) 
            

        
        return stack.pop() 
