class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                valA = int(stack.pop())
                valB = int(stack.pop())
                if token == '+':
                    stack.append(valA + valB)
                    continue
                if token == '*':
                    stack.append(valA * valB)
                    continue
                if token == '-':
                    stack.append(valB - valA)
                    continue
                if token == '/':
                    if valB == 0:
                        print(tokens)
                    stack.append(valB / valA)
                    continue
                else:
                    stack.append(valA)
                    stack.append(valB)
                    stack.append(int(token))
            else:
                stack.append(token)
        return int(stack.pop())
        