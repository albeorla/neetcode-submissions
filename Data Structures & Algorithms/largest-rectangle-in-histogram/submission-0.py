class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = []
        max_area: int = 0

        n: int = len(heights)
        for i in range(n+1):
            arriving: int = heights[i] if i < n else 0
            while stack and heights[stack[-1]] > arriving:
                top: int = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                width = right - left - 1
                area = heights[top] * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area