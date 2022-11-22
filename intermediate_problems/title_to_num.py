class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		result = 0
		for i in range(len(A)):
			print("result bf", result)
			result *= 26
			print("A[i]", A[i])
			print("val", ord(A[i]) - ord('A') + 1)
			result += ord(A[i]) - ord('A') + 1
			print("result", result)
		return result


A = "AAC"
s = Solution()
print(s.titleToNumber(A))