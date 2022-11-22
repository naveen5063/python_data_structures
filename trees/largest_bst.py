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
        path = []
        finallist = []
        self.get_all_paths(A, path, finallist)
        print("res", finallist)

    def get_all_paths(self, node, path, finallist):

        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            finallist.append(list(path))

        self.get_all_paths(node.left, path, finallist)
        self.get_all_paths(node.right, path, finallist)
        path.pop()

    def isValidBst(self, root):
        minval = 1 - sys.maxsize
        maxval = sys.maxsize
        countn = 0
        return  self.checkBstcount(root, minval, maxval, countn)
        print("countn", countn)

    def checkBst(self, root, minval, maxval):
        if root is None:
            return True
        # print("root.val", root.val)
        if root.val >= maxval or root.val <= minval:
            return False
        return self.checkBst(root.left, minval, root.val) and self.checkBst(root.right, root.val, maxval)

    def checkBstcountnew(self, root, minval, maxval, countn):
        if root is None:
            return True
        # print("root.val", root.val)
        if root.val >= maxval or root.val <= minval:
            return False
        elif root.val <= maxval or root.val >= minval:
            countn += 1
            print("count", countn)
        return self.checkBstcountnew(root.left, minval, root.val, countn) and self.checkBstcountnew(root.right, root.val, maxval, countn)

    def checkBstcount(self, root, minval, maxval, count):
        if root is None:
            #print("no", root)
            return 0


        # ("root.val", minval, "--", root.val, maxval)
        ls = self.checkBstcount(root.left, minval, root.val, count)
        rs = self.checkBstcount(root.right, root.val, maxval, count)
        if root.val >= maxval or root.val <= minval:
            return 0

        elif root.val <= maxval or root.val >= minval:
            count += 1
            print(root.val, "count", count)
        print("maxval", maxval, minval)
        print("count out", ls, rs, count)
        return max(ls, rs) + count


# Driver Code
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
    #root.left.left = newNode(1)
    root.right = newNode(12)
    root.left.left = newNode(11)
    s = Solution()
    print("--------", s.isValidBst(root))
