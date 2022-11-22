class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
		dp = [-1] * len(A)
		dp[0] = 1
		for i in range(1, len(A)):
			val = 0
			for j in range(0, i):
				if A[j] < A[i]:
					val = max(val, dp[j])
			dp[i] = val + 1
		return max(dp)


A = [1, 2, 1, 5]
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
s = Solution()
print(s.lis(A))

