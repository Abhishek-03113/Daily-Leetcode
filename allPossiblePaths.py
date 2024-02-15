def areAllVerticesEvenDegree(paths):
    for path in paths:
        if sum(path) % 2 != 0:
            return False
    return True
        
class Solution:
	def isPossible(self, paths):
		return int(areAllVerticesEvenDegree(paths))
