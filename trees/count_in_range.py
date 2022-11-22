# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A is None:
            return 0
        count = 0
        if B <= A.val <= C:
            count += 1
        count += self.solve(A.left, B, C)
        count += self.solve(A.right, B, C)
        return count


if __name__ == '__main__':
    root = TreeNode(8)
    #left tree
    root.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(12)
    root.left.right.right = TreeNode(9)
    root.left.right.right.right = TreeNode(4)
    #right tree
    root.right = TreeNode(6)
    root.right.right = TreeNode(10)

    # root = TreeNode(1)
    # root.left = TreeNode(15)
    # root.right = TreeNode(2)
    s = Solution()
    B = 5
    C = 8
    print(s.solve(root, B, C))
