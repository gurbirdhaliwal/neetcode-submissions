class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min = self.stack[-1]
            if val <= min:
                self.stack.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)
                self.stack.append(min)
        else:
            self.stack.append(val)
            self.stack.append(val)
        return self.stack


    def pop(self) -> None:
        if self.stack[-1] == self.stack[-2]:
            self.stack.pop(-1)
            self.stack.pop(-1)
        else:
            self.stack.pop(-2)
            self.stack.pop(-2)
        return

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]