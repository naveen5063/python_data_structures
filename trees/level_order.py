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
        while len(q) > 0:
            locallist = []
            for i in range(0, len(q)):
                front = q[0]
                q.remove(q[0])
                locallist.append(front.val)
                # if front is None:
                #     print("\n")
                #     if len(q) > 0:
                #         q.append(None)
                #     continue
                # print(front.val, end="")
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            res.append(locallist)
            #res.append("\n")
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(6)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.levelOrder(root))
