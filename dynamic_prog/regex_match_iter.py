import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
		rows = len(A)
		cols = len(B)
		dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
		dp[0][0] = 1
		for i in range(1, cols + 1):
			if B[i-1] == "*":
				dp[0][i] = 1
			else:
				break
		for i in range(1, rows + 1):
			for j in range(1, cols + 1):
				if A[i-1] == B[j - 1] or B[j - 1] == "?":
					dp[i][j] = dp[i - 1][j - 1]
				elif B[j - 1] == "*":
					dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

		return dp[rows][cols]

A = "aaa"
B = "a*"
A = "acz"
B = "a?a"
s = Solution()
print(s.isMatch(A, B))