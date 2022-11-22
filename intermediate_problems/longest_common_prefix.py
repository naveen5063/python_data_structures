import sys


class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
		minlen = sys.maxsize
		min_len_word = ""
		res = ""
		for ele in A:
			if len(ele) < minlen:
				minlen = len(ele)
				min_len_word = ele

		for i in range(minlen):
			flag = True
			for ele in A:
				if min_len_word[i] != ele[i]:
					flag = False
			if flag:
				res += min_len_word[i]

		print(res)


A = ["abcdefgh", "aefghijk", "abcefgh"]
#A = ["abab", "ab", "abcd"]

s = Solution()
print(s.longestCommonPrefix(A))