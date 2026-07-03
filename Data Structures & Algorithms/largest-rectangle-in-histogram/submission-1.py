class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        st = []
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                tp = st.pop()
                width = i if not st else i - st[-1] - 1
                max_area = max(max_area, heights[tp] * width)
            st.append(i)
        while st:
            tp = st.pop()
            width = n if not st else n - st[-1] - 1
            max_area = max(max_area, heights[tp] * width)
            
        return max_area