class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict() 
        for i in arr:
            hashmap[i] = 1 + hashmap.get(i, 0)
        seen = set() 
        
        for i in hashmap:
            if hashmap[i] in seen: 
                return False    
            else:
                seen.add(hashmap[i])
        return True



