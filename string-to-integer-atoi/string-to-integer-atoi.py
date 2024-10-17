class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        res = 0
        sign = 1
        
        if not s:
            return 0
        
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign = -1
            s = s[1:]
        
        for i in s:
            if not i.isdigit():
                break
            res = res * 10 + int(i)
        res = sign*res
        if res > 2**31-1:
            return 2**31-1
        elif res <-2**31:
            return -2**31
        
        return res
        
        
        