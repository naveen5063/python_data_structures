class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		hash_set = set()
		for i in range(0, len(A)):
			a = A[i]
			print(a, a - B, a + B, B)
			if a - B in hash_set or a + B in hash_set:
				# if b in hash_set:
				# 	print("b found", b)
				return 1
			else:
				hash_set.add(a)
		return 0


A = [1, 5,  3]
B = 2

A = [ 0 ]
B = 0

A = [ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ]
B = 53

#A = [ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]
#B = 97

s = Solution()
print(s.diffPossible(A, B))