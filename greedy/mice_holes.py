class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
		A.sort()
		B.sort()
		ans = 0
		for i in range(0, len(A)):
			ans = max(ans, abs(A[i] - B[i]))
		return ans



A = [-4, 2, 3]
B = [0, -2, 4]
s = Solution()
print(s.mice(A, B))