class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        closing_brackets = {')': 0, '}': 1, ']': 2}
        for i in range(len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            elif len(stack) > 0:
                local_peek = stack.pop()
                if open_brackets[closing_brackets.get(s[i])] != local_peek:
                    return False
            else:
                return False
        
        if stack:
            return False
        return True
        