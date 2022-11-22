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

    def sum(self, root):

        if root is None:
            return 0
        return (self.sum(root.left) +
                root.val +
                self.sum(root.right))

    # returns 1 if sum property holds
    # for the given node and both of
    # its children
    def isSumTree(self, node):

        # ls, rs

        # If node is None or it's a leaf
        # node then return true
        if (node is None or
                (node.left is None and
                 node.right is None)):
            return 1

        # Get sum of nodes in left and
        # right subtrees
        ls = self.sum(node.left)
        rs = self.sum(node.right)
        print("ls", ls)
        print("rs", rs)

        # if the node and both of its children
        # satisfy the property return 1 else 0
        print("node.val == ls + rs", node.val, node.val == ls + rs)
        if ((node.val == ls + rs) and
                self.isSumTree(node.left) and
                self.isSumTree(node.right)):
            print("true")
            return 1

        return 0


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(26)
    root.left = TreeNode(10)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(3)
    s = Solution()
    print(s.isSumTree(root))
