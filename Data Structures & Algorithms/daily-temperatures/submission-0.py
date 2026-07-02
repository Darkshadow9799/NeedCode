class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []  # Pairs of (index, temperature)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                ans[stack_i] = i - stack_i
            stack.append((i, t))
            
        return ans