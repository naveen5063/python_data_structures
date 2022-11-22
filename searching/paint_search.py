class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, A, B, C):
		ans = 0
		if B > 1:
			for i in range(0, len(C)):
				C[i] = C[i] * B
		low = max(C)
		high = sum(C)
		while low <= high:
			mid = int((low + high) / 2)
			if self.check(mid, C, len(C), A):
				ans = mid
				high = mid - 1
			else:
				low = mid + 1
		return ans % 10000003

	def check(self, mid, C, param, A):
		sum = 0
		count = 0
		print("c check", C, mid)
		for i in range(0, param):
			sum += C[i]
			print("sum ", sum)
			if sum > mid:
				sum = C[i]
				count += 1
				if count == A:
					return False
		return True


A = 10 # painters
B = 1 # tasks
C = [1, 8, 11, 3]
#
A = 2
B = 5
C = [1, 10]
s = Solution()
print(s.paint(A, B, C))