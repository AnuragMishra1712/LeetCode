class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 1
        
        
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[left] = nums[r]
                left+=1

        return left        

          

                
                
          
           

           