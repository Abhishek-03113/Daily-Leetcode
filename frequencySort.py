class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        hashmap = defaultdict() 

        for i in s: 
            hashmap[i] = 1 + hashmap.get(i,0)
        
        items = [(-freq,char) for char, freq in hashmap.items()]

        heapq.heapify(items)

        while items:
            freq, chars = heapq.heappop(items)
            ans += chars * -freq 

        
        return ans 
