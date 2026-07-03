class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            mid = start + (end - start) // 2
            print(mid)
            if (nums[mid] > target):
                end = mid - 1
            elif (nums[mid] < target):
                start = mid + 1
            else:
                return mid
        if start < len(nums) and nums[start] == target:
            return start
        elif end < len(nums) and nums[end] == target:
            return end
        return -1
