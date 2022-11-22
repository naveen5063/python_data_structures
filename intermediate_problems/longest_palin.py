class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):

		longest_palin_str_len = 0
		longest_palin_str = None

		def expand(input_str, start, end):
			while start >= 0 and end < len(input_str):
				if input_str[start] != input_str[end]:
					return input_str[start + 1:end]
				start -= 1
				end += 1
			return input_str[start + 1:end]

		for i in range(len(A)):
			odd_max = expand(A, i, i)
			even_max = expand(A, i, i+1)
			if len(odd_max) > longest_palin_str_len or len(even_max) > longest_palin_str_len:
				if len(odd_max) < len(even_max):
					longest_palin_str = even_max
					longest_palin_str_len = max(longest_palin_str_len, len(even_max))
				else:
					longest_palin_str = odd_max
					longest_palin_str_len = max(longest_palin_str_len, len(odd_max))
		return longest_palin_str

A = "aaaabaaa"
# "aaabaaa"
s = Solution()
print("out", s.longestPalindrome(A))