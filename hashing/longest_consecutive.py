class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
		hash_values = set(A)
		ans = 0
		for val in hash_values:
			if val - 1 not in hash_values:
				ele = val + 1
				count = 1
				while ele in hash_values:
					ele += 1
					count += 1
				ans = max(ans, count)
		return ans


A = [100, 4, 200, 1, 3, 2]
#  4
s = Solution()
print(s.longestConsecutive(A))