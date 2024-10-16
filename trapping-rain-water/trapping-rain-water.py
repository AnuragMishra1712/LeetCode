class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, len(height)-1
        leftmax,rightmax = height[l],height[r]
        res = 0
        if not height:
            return 0
        while l < r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax,height[l])
                res+= leftmax - height[l]
            else:
                r-=1
                rightmax = max(rightmax,height[r])
                res+= rightmax-height[r]
        return res        