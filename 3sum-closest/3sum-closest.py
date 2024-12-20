class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        nums.sort()
        closest_sum = float('inf')
    
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            
            while l<r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if abs(cur_sum -target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                
                if cur_sum == target:
                    return cur_sum
                elif cur_sum<target:
                    l+=1
                else:
                    r-=1
                
        return closest_sum       
    
    