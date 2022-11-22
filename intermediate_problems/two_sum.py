class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		hash_list = {}
		for i in range(0, len(A)):
			if B - A[i] in hash_list.keys():
				return [hash_list[B - A[i]]+1, i+1]
			else:
				if not A[i] in hash_list.keys():
					hash_list[A[i]] = i
		return -1



# Input: [2, 7, 11, 15], target = 9
# Output: index1 = 1, index2 = 2

A = [2, 7, 11, 15]
B = 9
s = Solution()
print("2sum", s.twoSum(A, B))