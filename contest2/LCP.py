class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return an integer
	def LCPrefix(self, A, B):
		mod = 1000000000+7
		for i in range(0, len(A)):
			A[i] = A[i][0:B]

		count = 1
		ans = 0
		for i in range(1, len(A)):
			if A[i] == A[i-1]:
				count += 1
			else:
				ans += (count * (count + 1)/2)
				count = 1
		ans += (count * (count + 1) / 2)
		return int(ans)


A = ["abc", "abdc", "abcba", "abcbd"]
B = 3
s = Solution()
print(s.LCPrefix(A, B))