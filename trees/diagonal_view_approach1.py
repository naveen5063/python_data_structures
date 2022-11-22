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
        level_dict = {}
        q.append([A, 0])
        minlevel = sys.maxsize
        maxlevel = 1 - sys.maxsize
        while len(q) > 0:
            p = q[0]
            t = p[0]
            q.popleft()
            level = p[1]
            minlevel = min(minlevel, level)
            maxlevel = max(maxlevel, level)
            if level not in level_dict.keys():
                level_dict[level] = [t]
            else:
                level_dict[level] += [t]

            #diagonal
            # if t.left is not None:
            #     q.append([t.left, level])
            # if t.right is not None:
            #     q.append([t.right, level + 1])

            # reverse diagonal
            if t.left is not None:
                q.append([t.left, level + 1])
            if t.right is not None:
                q.append([t.right, level])
        print("level_dict", level_dict)
        diagonalview = []
        for i in range(0, maxlevel + 1):
            temp = level_dict[i]
            for j in range(0, len(temp)):
                diagonalview.append(temp[j].val)
        return diagonalview


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(6)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(3)
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
    # #left tree
    # root.left = TreeNode(4)
    # root.left.left = TreeNode(8)
    # root.left.right = TreeNode(5)
    # root.left.right.left = TreeNode(9)
    # root.left.right.right = TreeNode(7)
    #
    # #right tree
    # root.right = TreeNode(2)
    # root.right.right = TreeNode(3)
    # root.right.right.left = TreeNode(6)


    # root = TreeNode(1)
    # root.left = TreeNode(15)
    # root.right = TreeNode(2)
    s = Solution()
    print(s.diagonalview(root))
