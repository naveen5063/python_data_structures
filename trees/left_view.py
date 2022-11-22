from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        res = []
        q = deque()
        q.append(A)
        #q.append(None)
        #res.append(A.val)
        while len(q) > 0:
            n = len(q)
            print("n", n)
            for i in range(0, n):
                front = q.popleft()
                #q.remove(q[0])
                if i == 0:
                    res.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
        return res

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.right = TreeNode(5)
    s = Solution()
    print(s.levelOrder(root))
