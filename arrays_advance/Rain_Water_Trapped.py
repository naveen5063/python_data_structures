class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
		pfm = self._get_prefix_max(A)
		sfm = self._get_sufix_max(A)
		res = 0
		for i in range(1, len(A)-1):
			left_max = pfm[i-1]
			right_max = sfm[i+1]
			h_level = min(left_max, right_max)
			w = max(h_level-A[i], 0)
			res += w
		return res

	def _get_prefix_max(self, A):
		pfm = [0]*len(A)
		pfm[0] = A[0]
		for i in range(1, len(A)):
			pfm[i] = max(pfm[i-1], A[i])
		return pfm

	def _get_sufix_max(self, A):
		sfm = [0] * len(A)
		sfm[-1] = A[-1]
		for i in range(len(A)-2, -1, -1):
			sfm[i] = max(sfm[i + 1], A[i])
		return sfm


A = [0, 1, 0, 2]
A = [1, 2]
#A = [1, -6, 3, 2, 8, 7]
#A = [3, 10, 6, 7, 0, 2, -1]
s = Solution()
print(s.trap(A))