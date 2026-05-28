class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        max_from_left = [0 for _ in range(size)]
        max_from_left[0] = height[0]
        max_from_right = [0 for _ in range(size)]
        max_from_right[0] = height[size-1]
        max_area_of_water = 0
        for i in range(1, size):
            max_from_left[i] = max(max_from_left[i-1], height[i])
            max_from_right[i] = max(max_from_right[i - 1], height[size - i - 1])
        max_from_right.reverse()
        
        for i in range(size):
            max_area_of_water += min(max_from_right[i], max_from_left[i]) - height[i]
        
        return max_area_of_water

        