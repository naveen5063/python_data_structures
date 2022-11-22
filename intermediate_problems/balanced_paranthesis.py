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

class Solution:
    # @param A : string
    # @return an integer
    ms = MinStack()
    def solve(self, A):
        count = 0
        for i in range(0, len(A)):
            if A[i] == "(":
                self.ms.push(A[i])
                count += 1
            if A[i] == ")":
                self.ms.pop()
                count -= 1
            # if self.ms.head_min:
            #     count += 1
        print("self.ms.top()", self.ms.top())
        print("count", count)
        if self.ms.top() == -1 and count >=0:
            return 1
        return 0
        # if self.ms.top() == -1:
        #     if count != 0:
        #         return 1
        #     return 0
        # return 0


#A = "(()())"
#A = "(()"
#A = ") ) ( ( ( ) ( ( ) )"
A = "()"
A = ")))"
A = ")))()"
s = Solution()
print(s.solve(A))