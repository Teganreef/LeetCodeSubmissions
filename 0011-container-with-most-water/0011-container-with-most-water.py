class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0 
        right = (len(height) - 1)
        best = 0 
        while left < right:
            maxArea = min(height[left],height[right]) * (right - left)
            best = max(best,maxArea)
            if height[left] >= height[right]:
                right -= 1 
            elif height[left] <= height[right]:
                left += 1 
        return best
            





            # logic for this if comput area left times right and then keep a max area found with the two placement positons and hten if left is less than right move left up oen and then opposoitie for riught and hten cauclate area comapare store if nesscary and then stop wehn tehy are equal... so 
        