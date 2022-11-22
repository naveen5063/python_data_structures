class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def connect(self, root):
        curr = root
        while curr.left is not None:
            temp = curr
            while temp is not None:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next
            curr = curr.left



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(10)
    root.right.left.left = TreeNode(9)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    s = Solution()
    print(s.connect(root))
