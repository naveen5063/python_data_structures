from collections import deque


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


# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(4)
    root.right.right = newNode(6)
    s = Solution()
    print(s.solve(root))
