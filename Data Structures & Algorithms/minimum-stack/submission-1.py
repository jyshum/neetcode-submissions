class MinStack:

    def __init__(self):
        # minStack operates through an array
        self.stack = []
        self.mins = [] # keeping track of the minimum value in the stack after every push or pop

    def push(self, val: int) -> None:
        self.stack.append(val)
        # keep track min when new elements get pushed
        if len(self.mins) == 0:
            self.mins.append(val) # first value
        else:
            # add the smaller element between the new val being pushed and latest element
            # this will make it so the last element in mins will be the smallest
            self.mins.append(min(val, self.mins[len(self.mins)-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop() 

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def getMin(self) -> int:
        # return the top of mins to find the smallest element
        return self.mins[len(self.mins)-1]
        

