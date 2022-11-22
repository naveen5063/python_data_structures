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
    def topview(self, A):
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
            if t.left is not None:
                q.append([t.left, level - 1])
            if t.right is not None:
                q.append([t.right, level + 1])
        print("level_dict", level_dict)
        topview = []
        for i in range(minlevel, maxlevel + 1):
            temp = level_dict[i]
            for j in range(0, 1):
                topview.append(temp[j].val)
        topview.sort()
        return topview


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
    print(s.topview(root))
