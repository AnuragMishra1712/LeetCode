class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = ''
        
        for i in s:
            if i.isalnum():
                ns += i.lower()
        return ns == ns[::-1]                
        