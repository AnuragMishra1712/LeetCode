class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1,n2 = len(s1),len(s2)
        
        count1 = [0]*26 #s1
        count2 = [0]*26 #s2
        
        if n1>n2:
            return False
        
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')]+=1
            count2[ord(s2[i]) - ord('a')]+=1
        
        if count1 == count2:
            return True
        
        for i in range(n1,n2):
            count2[ord(s2[i])-ord('a')]+=1
            count2[ord(s2[i-n1])-ord('a')]-=1
            if count1 == count2:
                return True
        return False    
        
        
           
        
        
        
        