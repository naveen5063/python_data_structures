# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        temp = A
        while temp is not None:
            if temp.left is not None:
                rightmost = temp.left
                while rightmost.right is not None:
                    rightmost = rightmost.right
                rightmost.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
        return A


# Driver Code
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    # root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    s = Solution()
    print(s.flatten(root).val)
