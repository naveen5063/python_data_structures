import sys


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        left = ~sys.maxsize
        right = sys.maxsize
        root = A[0]
        for i in range(1, len(A)):
            if A[i] > root:
                left = root
            else:
                right = root
            if A[i] < left or A[i] > right:
                return False
            root = A[i]
        return True

A = [4, 10, 5, 8]
s = Solution()
print(s.solve(A))
