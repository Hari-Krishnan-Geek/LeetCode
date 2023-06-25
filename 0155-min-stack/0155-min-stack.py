class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minimum = val
        else:
            minimum = min(val, self.stack[-1]["min"])
        obj = {
            "val": val,
            "min": minimum
        }
        self.stack.append(obj)
        

    def pop(self) -> None:
        obj = self.stack.pop()
        return obj["val"]
        

    def top(self) -> int:
        return self.stack[-1]["val"]
        

    def getMin(self) -> int:
        return self.stack[-1]["min"]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()