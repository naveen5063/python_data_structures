import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        dp = [[-1 for i in range(0, n + 1)] for j in range(0, n + 1)]
        return self.get_mcm(dp, A, 1, n - 1)

    def get_mcm(self, dp, A, i, j):
        if i == j:
            return 0

        if dp[i][j] == -1:
            mincost = sys.maxsize
            for k in range(i, j):
                left_cost = self.get_mcm(dp, A, i, k)
                right_cost = self.get_mcm(dp, A, k + 1, j)
                combined_cost = A[i - 1] * A[k] * A[j]
                mincost = min(mincost, left_cost + right_cost + combined_cost)
            dp[i][j] = mincost
        return dp[i][j]


A = [40, 20, 30, 10, 30]
s = Solution()
print(s.solve(A))
