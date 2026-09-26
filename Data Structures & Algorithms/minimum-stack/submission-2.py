from typing import List
class MinStack:
    """min stack"""
    min: List[int]
    stack: List[int]



    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        """push"""
        if len(self.min) == 0 or val < self.min[-1] or len(self.min) == 0:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        """pop"""
        if self.min[-1] == self.stack[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        """top"""
        return self.stack[-1]

    def getMin(self) -> int:
        """get min"""
        return self.min[-1]
