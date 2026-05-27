class Solution:
    def maxArea(self, heights: List[int]) -> int:
      p1, p2, max_area = 0, len(heights) - 1, -1
      
      while p1 < p2:
        
        height = min(heights[p1], heights[p2])
        width = p2 - p1
        area = height *  width
        max_area = max(max_area, area) 
        
        if heights[p1] < heights[p2]:
          p1 += 1
        else:
          p2 -= 1
        
      return max_area