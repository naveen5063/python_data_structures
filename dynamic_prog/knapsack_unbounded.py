import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        rows = len(B)
        cols = A
        dp = [[-1 for i in range(cols + 1)] for j in range(rows + 1)]
        return self.get_maxval(B, C, dp, rows, cols)

    def get_maxval(self, B, C, dp, i, j):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] == -1:
            # dont pick
            a = self.get_maxval(B, C, dp, i - 1, j)
            if j >= C[i - 1]:
                # pick if weight > than remaining weight
                a = max(a, self.get_maxval(B, C, dp, i, j - C[i - 1]) + B[i - 1])
            dp[i][j] = a
        return dp[i][j]

A = 10
B = [5]
C = [10]
A = 10
B = [6, 7]
C = [5, 5]
s = Solution()
print(s.solve(A, B, C))