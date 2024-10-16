class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sets = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l+=1
            sets.add(s[r])
            res = max(res,r-l+1)
        return res    
        