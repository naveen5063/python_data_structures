class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		# for i in range(0, len(A)):
		# 	count = 0
		# 	for j in range(0, len(A)):
		# 		if A[j] > A[i]:
		# 			count += 1
		# 	print("A[i]", A[i])
		# 	print("count", count)
		# 	if A[i] == count:
		# 		return 1
		# return 0
		A.sort()
		A.reverse()

		# int
		# last = 0;
		# int
		# count = 0;
		# for (int i=0; i < A.size(); i++) {
		# if (last == A.get(i)) {
		# count++;
		# }
		# if (i < (A.size()-1) & & A.get(i) != A.get(i+1)) {
		# last = i+1;
		# }
		# }
		# mylist = list(dict.fromkeys(A))
		print("A", A)
		last = 0
		count = 0
		for i in range(0, len(A)):
			if last == A[i]:
				count += 1
			if i < len(A) - 1 and A[i] != A[i+1]:
				last = i-1
			if count == A[i]:
				return 1
		return 0
#A = [3, 2, 1, 3]
#A = [ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2, 6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3, 6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3, -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5, 4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6, -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9, -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3, 6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5, -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10, 4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 ]
A = [ 6, 7, 5 ]
A = [ 5, 6, 2 ]
s = Solution()
print(s.solve(A))
