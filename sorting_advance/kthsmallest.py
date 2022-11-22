class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
		A = list(A)
		A.sort()
		print(A)
		if 0 < B <= len(A):
			return A[B-1]


A = [2, 1, 4, 3, 2]
B = 3

A = [1, 2]
B = 2
A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
B = 9
s = Solution()
print(s.kthsmallest(A, B))