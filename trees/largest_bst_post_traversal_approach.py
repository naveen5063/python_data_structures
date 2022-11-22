import sys
from collections import deque
import os


# Definition for a  binary tree node
class newNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def solve(self, A):
        def largest_bst(A):
            nonlocal result
            if not A:
                return [True, float('inf'), float('-inf'), 0]

            leftBST, leftMin, leftMax, leftSize = largest_bst(A.left)
            rightBST, rightMin, rightMax, rightSize = largest_bst(A.right)

            if leftBST and rightBST and leftMax < A.val < rightMin:
                result = max(result, leftSize + rightSize + 1)
                leftMin = A.val if leftMin == float('inf') else leftMin
                rightMax = A.val if rightMax == float('inf') else rightMax
                return [True, leftMin, rightMax, leftSize + rightSize + 1]
            else:
                return [False, float('inf'), float('-inf'), 0]
        result = 0
        largest_bst(A)
        return result


if __name__ == '__main__':
    root = newNode(20)
    root.left = newNode(14)
    # root.left.left = newNode(1)
    root.right = newNode(12)
    root.left.left = newNode(11)
    s = Solution()
    print("--------", s.solve(root))
