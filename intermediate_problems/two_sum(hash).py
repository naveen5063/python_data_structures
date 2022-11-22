import sys

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		hash_map = {}
		for val in range(0, len(A)):
			hash_map[val+1] = A[val]

		print(hash_map)
		pair = []
		val1 = sys.maxsize
		min_value = sys.maxsize
		for i in range(0, len(A)):
			a = A[i]
			b = B - a
			print(a, b, B)
			if b in hash_map.values():
				print(i)
				val1 = i
				b_value = list(hash_map.keys())[list(hash_map.values()).index(b)]
				min_value = min(b_value, min_value)

		if min_value:
			pair.append(val1)
			pair.append(min_value)
		return pair


# Input: [2, 7, 11, 15], target = 9
# Output: index1 = 1, index2 = 2


A = [2, 7, 11, 15, 11]
B = 9

s = Solution()
print(s.twoSum(A, B))