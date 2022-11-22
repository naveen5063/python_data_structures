from collections import deque


# Definition for a  binary tree node
class newNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def solve(self, A):
        hashsum = set()
        res = self.get_sum(A, hashsum)
        res = int(res/2)
        if res in hashsum:
            return 1
        else:
            return 0

    def get_sum(self, A, hashsum):
        if A is None:
            return 0
        leftsum = self.get_sum(A.left, hashsum)
        hashsum.add(leftsum)
        rightsum = self.get_sum(A.right, hashsum)
        hashsum.add(rightsum)
        val = leftsum + A.val + rightsum
        hashsum.add(val)
        return val


# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    # root.right.left = newNode(4)
    # root.right.right = newNode(6)
    s = Solution()
    out = s.solve(root)
    print(out)
