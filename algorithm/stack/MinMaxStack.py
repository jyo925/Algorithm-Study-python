# minimum값을 O(1) time complexity로 return이 가능한 Stack을 Design 하여라


class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append(val)
            self._min_stack.append(val)
            return

        min_num = self._min_stack[-1]
        self._stack.append(val)
        if val < min_num:
            self._min_stack.append(val)

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


minStack = MinStack()
minStack.push(5)
minStack.push(3)
minStack.push(2)
minStack.push(4)
minStack.push(9)
print(minStack.getMin(), end=' ')
