class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        diff = 0
        for i, n in enumerate(nums):
            diff = target - n
            if diff in maps:
                return [maps[diff],i]
            maps[n]= i    
        return    

