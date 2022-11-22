class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, A):
		res = 0
		candy_from_left = [1 for i in range(len(A))]
		candy_from_right = [1 for i in range(len(A))]

		for i in range(1, len(A)):
			if A[i] > A[i-1]:
				candy_from_left[i] = candy_from_left[i-1] + 1
			else:
				candy_from_left[i] = 1

		for j in range(len(A)-2, -1, -1):
			if A[j] > A[j+1]:
				candy_from_right[j] = candy_from_right[j+1] + 1
			else:
				candy_from_right[j] = 1

		for k in range(0, len(A)):
			res += max(candy_from_left[k], candy_from_right[k])
		return res




A = [1, 5, 2, 1]
#A = [1, 2]
s = Solution()
print(s.candy(A))