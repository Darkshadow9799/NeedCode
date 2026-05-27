class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sumData = numbers[start] + numbers[end]
            if sumData == target:
                return [start + 1, end + 1]
            else:
                if sumData > target:
                    end -= 1
                else:
                    start += 1
        return []
        