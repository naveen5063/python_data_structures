import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        rows = len(A)
        cols = len(A[0])
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        dp[0][0] = A[0][0]
        return self.get_unique_path(A, dp, rows - 1, cols - 1)

    def get_unique_path(self, A, dp, i, j):
        if i < 0 or j < 0:
            return sys.maxsize
        if dp[i][j] == -1:
            dp[i][j] = min(self.get_unique_path(A, dp, i - 1, j), self.get_unique_path(A, dp, i, j - 1)) + A[i][j]
        return dp[i][j]


A = [
    [1, 3, 2],
    [4, 3, 1],
    [5, 6, 1]
]
A = [
    [1, -3, 2],
    [2, 5, 10],
    [5, -5, 1]
]
s = Solution()
print(s.minPathSum(A))
