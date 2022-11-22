import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

class MinStack:
    # @param x, an integer
    # @return an integer

    def __init__(self):
        self.head = None
        self.head_min = None

    def push(self, x):
        if self.head is None:
            self.head = Node(x)
            self.head_min = Node(x)
        else:
            new_ele = Node(x)
            new_ele.next = self.head
            self.head = new_ele
            if new_ele.val < self.head_min.val:
                new_min_ele = Node(x)
                new_min_ele.next = self.head_min
                self.head_min = new_min_ele
            else:
                tmp = self.head_min
                self.head_min = tmp
                tmp.next = self.head_min
        return

    def pop(self):
        if self.head is None:
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            self.head_min = self.head_min.next
            return tmp.val

    def top(self):
        if self.head is not None:
            return self.head.val
        return -1

    def getMin(self):
        # min = sys.maxsize
        # tmp = self.head
        # while tmp is not None:
        #     if tmp.val < min:
        #         min = tmp.val
        #     tmp = tmp.next
        # if min != sys.maxsize:
        if self.head_min is not None:
            return self.head_min.val
        return -1

    def print_ll(self):
        if self.head == None:
            return None
        else:
            current = self.head
            while current.next:
                print(current.val, end=" ")
                current = current.next
            print(current.val)

#self = linkedList()
s = MinStack()
s.push(1)
s.push(2)
s.push(-2)
print("min", s.getMin())
print("pop", s.pop())
s.print_ll()
print("min", s.getMin())
print("top", s.top())
# print(s.getMin())
# print(s.pop())
# print(s.top())