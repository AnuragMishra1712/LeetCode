from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        gmap = defaultdict(list)
        res = []
        
        for i in strs:
            sorted_strs = tuple(sorted(i))
        
            gmap[sorted_strs].append(i)
            
        for values in gmap.values():
            res.append(values)
        
        
        

            
        
        return res