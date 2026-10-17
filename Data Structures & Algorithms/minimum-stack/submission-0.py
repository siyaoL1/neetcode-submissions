class MinStack:

    def __init__(self):
        self.stack = []
        self.previous_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.previous_min or (
            self.previous_min and self.previous_min[-1] >= val):
            self.previous_min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.previous_min and self.previous_min[-1] == val:
            self.previous_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.previous_min[-1]
