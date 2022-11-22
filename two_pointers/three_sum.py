class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def threeSum(self, A):
		p1 = 0
		p2 = 1
		p3 = 2
		res = []
		while p3 < len(A):
			print("A[p1] + A[p2] + A[p3] ", A[p1], A[p2] , A[p3] )
			if A[p1] + A[p2] + A[p3] == 0:
				res.append(list([A[p1], A[p2], A[p3]]))
				p1 += 1
			elif A[p1] + A[p2] + A[p3] < 0:
				p1 += 1
				p3 += 1
			else:
				p2 += 1
				p3 += 1
		print("res", res)


A = [-1, 0, 1, 2, -1, 4]
s = Solution()
s.threeSum(A)