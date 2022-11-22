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
    #def lca(self, A, B, C):

        # if A is None:
        #     return 0
        # if B <= A.val <= C or B >= A.val >= C:
        #     return A.val
        # if A.val > B and A.val > C:
        #     return self.lca(A, B, C)
        # elif A.val < B and A.val < C:
        #     return self.lca(A, B, C)
        # else:
        #     return A.val

    def lca(self, A, B, C):
        b_path = self.solve(A, B)
        c_path = self.solve(A, C)
        if b_path and c_path:
            for i in range(0, min(len(b_path), len(c_path))):
                if b_path[i] is not c_path[i]:
                    break
                elif i == min(len(b_path), len(c_path)) - 1:
                    return b_path[i]
            if b_path and c_path:
                return b_path[i - 1]
        else:
            return -1

    def solve(self, A, B):

        path = []
        self.get_path(A, B, path)
        path.reverse()
        return path

    def get_path(self, A, B, path):

        if A is None:
            return False

        if A.val == B:
            path.append(A.val)
            return True

        if self.get_path(A.left, B, path) or self.get_path(A.right, B, path):
            path.append(A.val)
            return True
        else:
            return False

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
    root = TreeNode(8)
    root.left = TreeNode(9)
    root.right = TreeNode(6)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(12)
    s = Solution()
    print(s.lca(root, 9, 2))
