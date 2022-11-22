from collections import deque

# Definition for a  binary tree node
class newNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        res = []
        q = deque()
        q.append(A)
        while len(q) > 0:
            tmp = q.popleft()
            if tmp is None:
                res.append(-1)
                continue
            res.append(tmp.val)
            q.append(tmp.left)
            q.append(tmp.right)
        return res




# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(4)
    root.right.right = newNode(6)
    s = Solution()
    print(s.solve(root))