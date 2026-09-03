class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # append the element to the stack
        # append it as a tuple but if the stack is empty append the value itself
        # otherwise append the value and the min of current min and the value itself
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))


    def pop(self) -> None:
        # remove the last element of the stack list
        # it returns nothing
        self.stack.pop()

    def top(self) -> int:
        # return the first element of the last tuple in the stack list
        return self.stack[-1][0]

    def getMin(self) -> int:
        # return the second element of the last tuple in the stack list
        return self.stack[-1][1]