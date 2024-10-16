class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        res = 0
        while l<r:
            area = min(height[l],height[r])*(r-l)
            res= max(res,area)
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]: 
                l+=1
            else:
                l+=1
        return res        