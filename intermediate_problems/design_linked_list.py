
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list

    size = 0

    def solve(self, A):
        print(A)
        for i in range(0, len(A)):
            print("A[i][0]", A[i][0])
            if A[i][0] == 0:
                self.insertAtFirst(A[i][1])
            elif A[i][0] == 1:
                self.insertAtLast(A[i][1])
            elif A[i][0] == 2:
                self.addNode(A[i][1], A[i][2])
            elif A[i][0] == 3:
                self.deleteAtPos(A[i][2], A[i][1])
        #self.print_ll()
        return llist.head

    def insertAtFirst(self, ele):
        print("insertAtFirst")
        if llist.head is None:
            llist.head = Node(ele)
        else:
            new_ele = Node(ele)
            new_ele.next = llist.head
            llist.head = new_ele
        Solution.size += 1

    def insertAtLast(self, ele):
        print("insertAtLast")
        new_ele = Node(ele)
        tmp = llist.head
        if llist.head is None:
            llist.head = new_ele
        else:
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new_ele
        Solution.size += 1

    def addNode(self, ele, index):
        print("addNode")
        if index == Solution.size:
            self.insertAtLast(ele)
        elif index == 0:
            self.insertAtFirst(ele)
        elif index > Solution.size or index < 0:
            return
        else:
            self.addAtIndex(ele, index)

    def addAtIndex(self, ele, index):
        print("addAtIndex")
        count = 0
        new_node = Node(ele)
        tmp = llist.head
        while count < index - 1:
            tmp = tmp.next
            count += 1
        new_node.next = tmp.next
        tmp.next = new_node
        Solution.size += 1

    def deleteAtPos(self, ele, pos):
        print("deleteAtPos")
        if llist.head is None:
            return
        tmp = llist.head
        if pos < Solution.size:
            if pos == 0:
                llist.head = llist.head.next
            else:
                for k in range(0, pos - 1):
                    tmp = tmp.next
                tmp.next = tmp.next.next
            Solution.size -= 1

    # def print_ll(self):
    #     # Output each element followed by a space
    #     if llist.head is None:
    #         return None
    #     else:
    #         current = llist.head
    #         while current.next:
    #             print(current.val, end="->")
    #             current = current.next
    #         print(current.val, end="->")
    #         print("NULL")


# Input 1:
A = [[0, 1, -1],
     [1, 2, -1],
     [2, 3, 1]]

# A = [   [0, 1, -1],
#             [1, 2, -1],
#             [2, 3, 1],
#             [0, 4, -1],
#             [3, 1, -1],
#             [3, 2, -1]
#                        ]
#
# A =[
#   [2, 18, 0],
#   [2, 5, 1],
#   [2, 8, 0],
#   [1, 7, -1],
#   [1, 5, -1],
# ]
#
# A =[
#   [1, 13, -1],
#   [3, 0, -1],
#   [3, 1, -1],
#   [2, 15, 0],
#   [3, 0, -1],
#   [1, 12, -1],
#   [3, 0, -1],
#   [1, 19, -1],
#   [1, 13, -1],
#   [3, 0, -1],
#   [0, 12, -1],
#   [1, 13, -1],
#   [3, 2, -1]
# ]
#
# A =[
#   [2, 18, 0],
#   [2, 5, 1],
#   [2, 8, 0],
#   [1, 7, -1],
#   [1, 5, -1]
# ]
# Output
# 1:
# 1->3->2->NULL
def print_ll(self):
    # Output each element followed by a space
    if llist.head is None:
        return None
    else:
        current = llist.head
        while current.next:
            print(current.val, end="->")
            current = current.next
        print(current.val, end="->")
        print("NULL")

llist = LinkedList()
s = Solution()
out = s.solve(A)
print_ll(out)
