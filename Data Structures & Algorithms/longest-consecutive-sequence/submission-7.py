class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(list(set(nums)))
        max_val = 1
        for i in range(0, len(nums)):
            local_max = 1
            for j in range(i+1, len(nums)):
                if (nums[j] == nums[j-1] or nums[j] == nums[j-1] + 1):
                    local_max += 1
                else:
                    i = j
                    break
            max_val = max(max_val, local_max)
        return max_val
        