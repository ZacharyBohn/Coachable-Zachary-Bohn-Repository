class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        return

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]   

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
