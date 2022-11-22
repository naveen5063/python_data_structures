class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        rows = len(A)
        cols = C
        dp = [[-1 for i in range(cols + 1)] for j in range(rows + 1)]
        return self.get_maxval(A, B, dp, rows, cols)

    def get_maxval(self, A, B, dp, i, j):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] == -1:
            # dont pick
            a = self.get_maxval(A, B, dp, i - 1, j)
            if j >= B[i - 1]:
                # pick if weight > than remaining weight
                a = max(a, self.get_maxval(A, B, dp, i - 1, j - B[i - 1]) + A[i - 1])
            dp[i][j] = a
        return dp[i][j]


A = [60, 100, 120]
B = [10, 20, 30]
C = 50
A = [10, 20, 30, 40]
B = [12, 13, 15, 19]
C = 10
s = Solution()
print(s.solve(A, B, C))
