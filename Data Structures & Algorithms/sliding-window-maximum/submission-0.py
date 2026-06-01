class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        # edge case
        if len(nums) < k:
            return result
        
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i: i+k]))
        
        return result
