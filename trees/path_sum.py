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

    def hasPathSum(self, A, B):
        #return self.check_value(A, B)
        if self.check_path_sum(A, B, 0):
            return 1
        return -1

    def check_path_sum(self, A, B, C):
        if A is None:
            return False
        C += A.val
        if A.left == None and A.right == None:
            return C == B
        l = self.check_path_sum(A.left, B, C)
        r = self.check_path_sum(A.right, B, C)
        return l or r

    def check_value(self, A, B):
        if A is None:
            return False
        if A.val == B:
            return True
        return self.check_value(A.left, B) or self.check_value(A.right, B)


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    s = Solution()
    root = TreeNode(1000)
    root.left = TreeNode(200)
    print(s.hasPathSum(root, 1200))
