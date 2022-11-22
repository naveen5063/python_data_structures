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
        root = newNode(A[0])
        i = 1
        q = deque()
        q.append(root)
        while len(q) > 0:
            tmp = q.popleft()
            if A[i] != -1:
                tmp.left = newNode(A[i])
                q.append(tmp.left)
            i += 1
            if A[i] != -1:
                tmp.right = newNode(A[i])
                q.append(tmp.right)
            i += 1
        return root

# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(4)
    root.right.right = newNode(6)
    s = Solution()
    A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
    print(s.solve(A))