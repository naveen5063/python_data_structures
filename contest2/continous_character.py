class Solution:
	# @param A : string
	# @param B : integer
	# @param C : string
	# @return an integer
	def solve(self, A, B, C):
		ans = 0
		otherchar = 0
		right = -1
		for i in range(0, len(A)):
			#print("right", right, i)
			while right + 1 < len(A):
				if A[right + 1] is not C:
					otherchar += 1
				if otherchar <= B:
					right += 1
				else:
					otherchar -= 1
					break
			#print("right-i+1", right, i, otherchar, right-i+1)
			ans = max(ans, right-i+1)
			#print("A[i]", A[i])
			if A[i] is not C:
				otherchar -= 1
		return ans

A = "oyorooms"
B = 1
C = "o"
A = "abacus"
B = 2
C = "a"
s = Solution()
print(s.solve(A, B, C))
