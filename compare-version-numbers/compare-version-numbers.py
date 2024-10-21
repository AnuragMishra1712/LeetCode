class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = version1.split('.')
        v2 = version2.split('.')
       
        
        l1 = len(v1)
        l2 = len(v2)
        
        for i in range(max(l1,l2)):
            i1 = int(v1[i]) if i<l1 else 0
            i2 = int(v2[i]) if i<l2 else 0
            
            if i1!=i2:
                return 1 if i1>i2 else -1
        
        return 0
            