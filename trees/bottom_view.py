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
    def bottomview(self, A):
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
        bottomview = []
        for i in range(minlevel, maxlevel + 1):
            temp = level_dict[i]
            print("temp", temp)
            for j in range(0, 1):
                bottomview.append(temp[-1].val)
        #topview.sort()
        return bottomview


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
    print(s.bottomview(root))
