class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])

            else:
                if not stack or stack.pop() != pairs[s[i]]:
                    return False
        return len(stack) == 0
        