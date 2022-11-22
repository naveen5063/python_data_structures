class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
		rows = len(A)
		cols = len(A[0])
		if A[0][0] == 1:
			return 0
		dp = [[-1 for i in range(cols)] for j in range(rows)]

		dp[0][0] = 1
		res = self.get_unique_path(A, dp, rows - 1, cols - 1)
		print(dp)
		return res

	def get_unique_path(self, A, dp, i, j):
		if i < 0 or j < 0:
			return 0
		if A[i][j] == 1:
			return 0
		if dp[i][j] == -1:
			dp[i][j] = self.get_unique_path(A, dp, i - 1, j) + self.get_unique_path(A, dp, i, j - 1)
		#print("dp ---", dp)
		return dp[i][j]

A = [
	[0, 0, 0],
	[0, 1, 0],
	[0, 0, 0]
]
# A = [
#         [0, 0, 0],
#         [1, 1, 1],
#         [0, 0, 0]
#      ]
# A =[
#   [0, 0]
# ]
# #
# A = [
#   [1, 0]
# ]
s = Solution()
print(s.uniquePathsWithObstacles(A))