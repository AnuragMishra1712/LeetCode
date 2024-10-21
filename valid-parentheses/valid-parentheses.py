class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        cto = {")":"(","}":"{","]":"["}
        
        for i in s:
            if i in cto:
                if stack and stack[-1]==cto[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False        

        