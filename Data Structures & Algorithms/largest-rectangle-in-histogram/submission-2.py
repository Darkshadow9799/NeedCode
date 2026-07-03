class Solution:
    def getHeightAndWidth(self, st, pos):
        return st.pop(), pos if not st else pos - st[-1] - 1

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        st = []
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                tp, width = self.getHeightAndWidth(st, i)
                max_area = max(max_area, heights[tp] * width)
            st.append(i)
        while st:
            tp, width = self.getHeightAndWidth(st, n)
            max_area = max(max_area, heights[tp] * width)
            
        return max_area

    