class Solution:
	# @param A : tuple of integers
	# @return an integer

	def check_bit(self, A, i):
		return (A >> i) & 1 == 1


	def hammingDistance(self, A):
		sum = 0
		con = 0
		mod = 1000000007
		for i in range(0, 30):
			set = 0
			unset = 0
			for j in range(0, len(A)):
				if self.check_bit(A[j], i):
					set += 1
				else:
					unset += 1
			print(set, unset)
			con = ((set % mod) * (unset % mod)) % mod
			sum += con % mod
			print("con", con)
			print("sum", sum)
		return (2 * sum) % mod

A = [2, 4, 6]

A = [3, 3, 3]

A = [ 96, 96, 7, 81, 2, 13 ]

A = [8, 6, 2, 4]
#104

# We
# return,
# f(2, 2) + f(2, 4) + f(2, 6) +
# f(4, 2) + f(4, 4) + f(4, 6) +
# f(6, 2) + f(6, 4) + f(6, 6) =
#
# 0 + 2 + 1
# 2 + 0 + 1
# 1 + 1 + 0 = 8

s = Solution()
print(s.hammingDistance(A))

