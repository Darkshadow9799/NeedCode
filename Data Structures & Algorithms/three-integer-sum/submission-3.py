class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()
        numsLen = len(nums)
        for i in range(numsLen - 2):
            j = i + 1
            k = numsLen - 1
            while(j < k):
                sumData = nums[i] + nums[j] + nums[k]
                if (sumData == 0 and [nums[i], nums[j], nums[k]] not in result):
                    result.append([nums[i], nums[j], nums[k]])
                    # break
                elif (sumData > 0):
                    k -= 1
                else:
                    j += 1
        return result