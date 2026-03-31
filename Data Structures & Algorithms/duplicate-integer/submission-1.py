class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # setNums = set(nums)
        return len(set(nums)) != len(nums)
        