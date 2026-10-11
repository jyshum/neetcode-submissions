class MinStack:

    def __init__(self):
        # minStack operates through an array
        self.stack = []
        self.orders = {}

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        else:
            return null

    def getMin(self) -> int:
        # binary search to get min?
        return min(self.stack)
