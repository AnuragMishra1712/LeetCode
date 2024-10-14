class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maps = {}

        for i in nums:
            maps[i] = 1 + maps.get(i,0)
        # print(maps)
        freq = []
        for num,cnt in sorted(maps.items()):
            freq.append([cnt,num])
        freq.sort()    
            
        res = []  
        for c in range(len(freq)):
            if len(res) < k :
                res.append(freq.pop()[1])
        return res        

        
