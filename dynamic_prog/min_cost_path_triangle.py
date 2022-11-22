import sys
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        rows = len(A)
        cols = len(A[rows-1])
        dp = [[-1 for i in range(j+1)] for j in range(rows)]
        dp[rows-1][cols-1] = A[rows-1][cols-1]
        return self.get_unique_path(A, dp, rows, cols, 0, 0)

    def get_unique_path(self, A, dp, n, m, i, j):
        if i == n:
            return 0
        if dp[i][j] == -1:
            a = self.get_unique_path(A, dp, n, m, i + 1, j)
            b = self.get_unique_path(A, dp, n, m, i + 1, j + 1)
            dp[i][j] = min(a, b) + A[i][j]
        return dp[i][j]


A = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
A = [ [1] ]
s = Solution()
print(s.minimumTotal(A))
