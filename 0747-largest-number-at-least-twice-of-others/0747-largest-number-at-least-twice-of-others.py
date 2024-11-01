class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_num = sorted(nums)

        if sorted_num[-1]>=sorted_num[-2]*2:
            return nums.index(sorted_num[-1])
        else:
            return -1    