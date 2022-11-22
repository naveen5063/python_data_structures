class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
		hm = set()
		uniq = set()
		max_len = 0
		sub_len = 0

		if len(A) == 1:
			return 1

		for i in range(0, len(A)):
			print("A[i]", A[i])
			print("hm", hm)
			print("uniq", uniq)
			if A[i] in hm:
				print("A[i] pre", A[i])
				print("sub", sub_len)
				hm.remove(A[i])
				#hm = set()
				#sub_len -= 1
				max_len = max(max_len, sub_len)
				#sub_len = 0
			else:
				print("hm else", hm)
				hm.add(A[i])
				uniq.add(A[i])
				if A[i] not in uniq:
					sub_len += 1
				print("sub out", sub_len)
				max_len = max(max_len, sub_len)

		#print("mac", max_len)
		return max_len



A = "abcabcbb"
#A = "AaaA"
#A = "u"
#A = "dadbc"
s = Solution()
print(s.lengthOfLongestSubstring(A))