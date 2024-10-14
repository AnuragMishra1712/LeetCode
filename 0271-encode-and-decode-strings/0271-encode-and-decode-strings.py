class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for i in strs:
            res+= str(len(i)) + '#' + i
        return res    
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res,i = [],0
        
        while i < len(s):
            j = i
            while s[j]!= '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            res.append(s[i:length + j+1])
            i = j+1+length
            j=i
        return res   
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))