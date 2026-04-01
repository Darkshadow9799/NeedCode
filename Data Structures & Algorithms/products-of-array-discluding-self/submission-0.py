class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        suffix = 1
        for i in range(n):
            output[i] = suffix
            suffix *= nums[i]
        print(output)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1): 
            output[i] = output[i] * suffix
            suffix *= nums[i]
        return output