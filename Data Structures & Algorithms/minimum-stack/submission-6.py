class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.minimum:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
