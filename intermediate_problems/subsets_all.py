class Solution:
	# @param A : list of integers
	# @return a list of list of integers

	def checkbit(self, i, j):
		return (i >> j) & 1 == 1

	def subsets(self, A):
		A.sort()
		subset_all = []
		for i in range(0, 1 << len(A)):
			subset_arr = []
			for j in range(0, len(A)):
				if self.checkbit(i, j):
					subset_arr.append(A[j])
			subset_all.append(subset_arr)
		subset_all.sort()
		print("subset_all", subset_all)
		return subset_all

	# def subsets(self, l):
	# 	l.sort()
	# 	lists = [[]]
	# 	for i in range(len(l) + 1):
	# 		for j in range(i):
	# 			lists.append(l[j: i])
	# 	return lists


A = [1]
A = [1, 2, 3]
#[[], [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
#[[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
A = [ 15, 20, 12, 19, 4 ]
s = Solution()
print(s.subsets(A))