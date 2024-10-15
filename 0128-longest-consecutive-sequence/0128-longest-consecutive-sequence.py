class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        s = set(nums)
        
        for num in nums:
            if (num-1) not in s:
                next_num = num+1
                length = 1
                while next_num in s:
                    length+=1
                    next_num+=1
                longest = max(longest,length)
        return longest        
        
        
   