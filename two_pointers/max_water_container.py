class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A):
		p1 = 0
		p2 = len(A) - 1
		max_area = 0
		while p1 < p2:
			height = min(A[p1], A[p2])
			width = p2 - p1
			area = height * width
			max_area = max(area, max_area)
			if height == A[p1]:
				p1 += 1
			else:
				p2 -= 1
		return max_area

A = [1, 5, 4, 3]
# 6
s = Solution()
print(s.maxArea(A))