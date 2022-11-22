# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
import sys


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    from collections import deque
    def diagonalview(self, A):
        q = deque()
        q.append(A)
        ans = []
        while len(q) > 0:
            length = len(q)
            for i in range(length):
                node = q[0]
                q.popleft()
                while node is not None:
                    ans.append(node.val)
                    if node.left is not None:
                        q.append(node.left)
                    node = node.right
        return ans


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    # root = TreeNode(8)
    # root.left = TreeNode(9)
    # root.right = TreeNode(6)
    # root.right.left = TreeNode(2)
    # root.right.left.left = TreeNode(12)
    # root = TreeNode(1)
    # root.left = TreeNode(15)
    # root.right = TreeNode(2)
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(6)
    s = Solution()
    print(s.diagonalview(root))
 #[1, 2, 3, 4, 5, 7, 6, 8, 9]