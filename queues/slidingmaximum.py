from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
		start = 0
		ans = []
		queue = deque()
		for i in range(0, B):
			while len(queue) > 0 and A[i] > A[queue[-1]]:
				queue.remove(queue[-1])
			queue.append(i)

		ans.append(A[queue[0]])
		start += 1
		for i in range(B, len(A)):
			while len(queue) > 0 and A[i] > A[queue[-1]]:
				queue.remove(queue[-1])
			queue.append(i)
			if start > queue[0]:
				queue.remove(queue[0])
			ans.append(A[queue[0]])
			start += 1
		return ans

A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
s = Solution()
print(s.slidingMaximum(A, B))