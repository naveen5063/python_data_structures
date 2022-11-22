from collections import deque
class MyQueue:
    from collections import deque
    def __init__(self):
        from collections import deque
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        if len(self.stack2) > 0:
            return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2[-1]
        if len(self.stack1) > 0:
            return self.stack1[0]

    def empty(self) -> bool:
        if len(self.stack1) <= 0 and len(self.stack2) <= 0:
            return True
        else:
            return False

obj = MyQueue()
obj.push(10)
obj.push(20)
obj.push(30)
print("peek", obj.peek())
print("pop", obj.pop())
print("peek", obj.peek())
print("peek ", obj.pop())
print("peek", obj.peek())
# #param_4 = obj.empty()