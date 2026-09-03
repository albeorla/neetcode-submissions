class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = []

        wall = 0
        for i in range(len(height)):
            wall = max(wall, height[i])
            left_wall.append(wall)

        right_wall = [0] * len(height)
        wall = 0
        for i in range(len(height)-1, -1, -1):
            wall = max(wall, height[i])
            right_wall[i] = wall
    
        total = 0
        for i in range(len(height)):
            total += min(left_wall[i], right_wall[i]) - height[i]

        return total