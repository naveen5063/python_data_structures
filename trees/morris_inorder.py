#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        current = A
        while current is not None:
            if current.left is None:
                print(current.val)
                current = current.right
            else:
                temp = current.left
                while temp.right is not None and temp.right is not current:
                    temp = temp.right

                if temp.right is None:
                    temp.right = current
                    current = current.left

                if temp.right is current:
                    temp.right = None
                    print(current.val)
                    current = current.right



if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(22)
    s = Solution()
    s.inorderTraversal(root)