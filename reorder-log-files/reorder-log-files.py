class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        digit,letter,res = [],[],[]
        
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log.split())
        letter.sort(key =lambda x:x[:1])
        letter.sort(key =lambda x:x[1:])
        
        for i in range(len(letter)):
            letter[i] = " ".join(letter[i])
        
        letter.extend(digit)
        
        return letter
        
        
        