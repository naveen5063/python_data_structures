import sys


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def calculateMinimumHP(self, A):
		rows = len(A)
		cols = len(A[0])
		dp = [[-1 for i in range(cols)]for j in range(rows)]
		dp[rows - 1][cols - 1] = max(1, 1 - A[rows - 1][cols - 1])
		return self.get_min_health(A, dp, rows, cols, 0, 0)

	def get_min_health(self, A, dp, n, m, i, j):
		if i == n or j == m:
			return sys.maxsize

		if dp[i][j] == -1:
			right_health = self.get_min_health(A, dp, n, m, i, j + 1)
			bottom_health = self.get_min_health(A, dp, n, m, i + 1, j)
			dp[i][j] = max(1, min(right_health, bottom_health) - A[i][j])
		return dp[i][j]



A = [
	[-2, -3, 3],
	[-5, -10, 1],
	[10, 30, -5]
]
s = Solution()
print(s.calculateMinimumHP(A))