class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        gmaps = {}
        maxc = 0
        para = paragraph.lower()
        banned = set(banned)
        symbols = "!?',;." 
        for s in symbols:
            para = para.replace(s," ")
        para = para.split()
         

        for i in para:
            if i not in banned:
                gmaps[i] = 1 + gmaps.get(i,0)      
        maxc = max(gmaps.values())
        
        for w,c in gmaps.items():
            if c == maxc:
                return w
            
                     
                    
                
        
                
                
                
                
                 
            
        