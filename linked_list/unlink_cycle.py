# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        s = A
        f = A

        while s and f:
            s = s.next
            f = f.next.next
            if s == f:
                break

        if s is None:
            return None

        p1 = A
        p2 = s

        while p1.next != p2.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = None
        return A