class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sym = { "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 } 
        res = 0
        
        for i in range(len(s)):
            if i+1 <len(s) and sym[s[i]] < sym[s[i+1]]:
                res-=sym[s[i]]
            else:
                res+=sym[s[i]]
        return res        
