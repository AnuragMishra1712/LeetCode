class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        gmaps = {}
        
        for i in s:
            gmaps[i] = gmaps.get(i,0)+1
            
        for idx,letter in enumerate(s):
            if gmaps[letter] == 1:
                return idx
        return -1        
        
      
      
            
            
        