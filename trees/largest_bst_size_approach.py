import sys
from collections import deque
import os


# Definition for a  binary tree node
class newNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def solve(self, A):
        return self.largestBST(root)

    def largestBST(self, root):
        if root is None:
            return 0

        if self.isValidBst(root):
            return self.size(root)

        return max(self.largestBST(root.left), self.largestBST(root.right))

    def isValidBst(self, root):
        minval = 1 - sys.maxsize
        maxval = sys.maxsize
        return self.checkBst(root, minval, maxval)

    def checkBst(self, root, minval, maxval):
        if root is None:
            return True
        if root.val >= maxval or root.val <= minval:
            return False
        return self.checkBst(root.left, minval, root.val) and self.checkBst(root.right, root.val, maxval)

    def size(self, root):
        if root is None:
            return 0
        ls = self.size(root.left)
        rs = self.size(root.right)
        return ls + rs + 1


if __name__ == '__main__':
    # root = newNode(7)
    # root.left = newNode(2)
    # #root.left.left = newNode(1)
    # root.right = newNode(5)
    # root.right.left = newNode(4)
    # root.right.right = newNode(6)
    # root = newNode(1)
    # root.left = newNode(2)
    # #root.left.left = newNode(1)
    # root.right = newNode(3)
    # root.right.left = newNode(4)
    # root.right.left.right = newNode(5)
    root = newNode(20)
    root.left = newNode(14)
    # root.left.left = newNode(1)
    root.right = newNode(12)
    root.left.left = newNode(11)
    s = Solution()
    print("--------", s.solve(root))
