# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lca(self, A, B, C):
        b_path = self.solve(A, B)
        c_path = self.solve(A, C)
        count = 0
        print("path", b_path, c_path)
        print("path", len(b_path), len(c_path))
        if b_path and c_path:
            for i in range(0, min(len(b_path), len(c_path))):
                if b_path[i] is not c_path[i]:
                    break
                elif i == min(len(b_path), len(c_path)) - 1:
                    #count -= 1
                    i += 1
                    print("c", count)
            print("len(b_path)", len(b_path) - 1, i - 1)
            print("i", i)
            for j in range(len(b_path) - 1, i - 1, -1):
                count += 1
            print("c", count)

            print("i, len(c_path)", i, len(c_path))
            for k in range(i, len(c_path)):
                count += 1
            print("count", count)
            # if b_path and c_path:
            #     return b_path[i - 1]
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
    # root = TreeNode(8)
    # root.left = TreeNode(9)
    # root.right = TreeNode(6)
    # root.right.left = TreeNode(2)
    # root.right.left.left = TreeNode(12)
    root = TreeNode(32)
    root.left = TreeNode(25)
    root.right = TreeNode(46)
    root.left.left = TreeNode(17)
    root.left.right = TreeNode(27)
    root.right.left = TreeNode(40)
    root.right.right = TreeNode(49)
    root.left.left.left = TreeNode(9)
    s = Solution()
    print(s.lca(root, 9, 49))
