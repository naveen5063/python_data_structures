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
            if t.left is not None:
                q.append([t.left, level - 1])
            if t.right is not None:
                q.append([t.right, level + 1])
        diagonalview = []
        #print("min max", minlevel, maxlevel)
        print("level_dict", level_dict)
        for i in range(0, minlevel - 1, -1):
            #print("i", i, maxlevel + 1)
            #print("i, minlevel", i, minlevel - 1)
            #print("i, maxlevel", i, maxlevel + 1)
            for j in range(i, maxlevel + 1):
                if j in level_dict.keys():
                    temp = level_dict[j]
                    print("temp", temp)
                    print("level j", j)
                    if temp:
                        print(":temp[0].val", temp[0].val)
                        diagonalview.append(temp[0].val)
                        del temp[0]
                    if not temp:
                        del level_dict[j]

            level_dict[j] = temp
        # for val in level_dict.keys():
        #     if level_dict[val]:
        #         temp = level_dict[val]
        #         while len(temp) > 0:
        #             diagonalview.append(temp[0].val)
        #             del temp[0]
        print("diagonalview", diagonalview)
        print("level_dict",level_dict)
        return diagonalview


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
    # root = TreeNode(1)
    # root.left = TreeNode(15)
    # root.right = TreeNode(2)
    root = TreeNode(29)
    root.left = TreeNode(10)
    root.right = TreeNode(15)
    root.left.left = TreeNode(28)
    root.left.right = TreeNode(28)
    root.right.left = TreeNode(29)
    root.right.right = TreeNode(4)
    s = Solution()
    print(s.diagonalview(root))
