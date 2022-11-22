# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.max = ~sys.maxsize

    def solve(self, A):
        # leftheight = self.get_maxlen(A.left)
        # rightheight = self.get_maxlen(A.right)
        # return leftheight + rightheight + 2
        self.max = ~sys.maxsize
        self.get_maxlen(A)
        return self.max

    def get_maxlen(self, A):
        if A is None:
            return - 1
        l = self.get_maxlen(A.left)
        r = self.get_maxlen(A.right)
        path = l + r + 2
        self.max = max(path, self.max)
        return max(l, r) + 1

    # def get_maxlen(self, A):
    #     if A is None:
    #         return -1
    #     l = self.get_maxlen(A.left)
    #     r = self.get_maxlen(A.right)
    #     return max(l, r) + 1


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    s = Solution()
    print(s.solve(root))
