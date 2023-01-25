class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            height = heights[left] if heights[left] < heights[right] else heights[right]
            current_area = (right - left)*height
            
            max_area = current_area if current_area > max_area else max_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area