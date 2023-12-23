class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0  

        dir_map = {
            "N" : 1,
            "S" : -1, 
            "E" : 1, 
            "W" : -1 
        }

        visited = set() 

        visited.add((0,0))


        for i in path: 

            if i =="N" or i == "S":

                y += dir_map[i] 
            elif i == "E" or i == "W":

                x += dir_map[i]
            
            if (x,y) not in visited:
                visited.add((x,y))
            else:
                return True 
        
        return False 
        
