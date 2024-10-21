class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sums = sum(nums)
        print(sums)
        for i in range(len(nums)+1):
            res+=i
        return res - sums
            
            
                
        