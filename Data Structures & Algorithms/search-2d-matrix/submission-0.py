class Solution:
    def binarySearch(self, arr: List[int], target: int) -> int:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if (arr[mid] < target):
                start = mid + 1
            elif (arr[mid] > target):
                end = mid - 1
            else:
                return mid
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if (matrix[i][0] <= target) and (matrix[i][-1] >= target):
                idx = self.binarySearch(matrix[i], target)
                if idx == -1:
                    return False
                else:
                    return True
        
        return False