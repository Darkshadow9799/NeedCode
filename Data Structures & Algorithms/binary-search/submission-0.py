class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            mid = (end + start) // 2
            print(mid)
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target) and (mid != (mid+end) // 2):
                start = mid
            else:
                end = mid
        return -1
