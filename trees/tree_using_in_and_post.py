# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        global indexmap
        indexmap = {}
        for i in range(0, len(B)):
            indexmap[B[i]] = i
        return self.get_tree(A, 0, len(A) - 1, B, 0, len(B) - 1)

    def get_tree(self, B, prestart, preend, A, instart, inend):
        print("prestart, preend, instart, inend", prestart, preend, instart, inend)
        if prestart > preend:
            return None
        root = TreeNode(B[preend])
        print("root", root.val)
        idx = indexmap[root.val]
        n = idx - instart
        print("n", n)
        print("idx", idx)
        root.left = self.get_tree(B, prestart, prestart + n - 1, A, instart, idx - 1)
        print("right")
        root.right = self.get_tree(B, prestart + n + 1, preend - 1, A, idx + 1, inend)
        return root


s = Solution()
A = [1]
B = [1]
A = [2, 1, 3]
B = [2, 3, 1]

res = s.buildTree(A, B)
print(res.val)
print(res.left.val)
print(res.right)
