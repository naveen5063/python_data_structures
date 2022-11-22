import sys


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        hs = set()
        max_len = 1 - sys.maxsize

        if len(A) == 1:
            return 1

        i = 0
        j = 0
        while j < len(A):
            if A[j] in hs:
                while A[j] in hs:
                    hs.remove(A[i])
                    i += 1
            else:
                hs.add(A[j])
                max_len = max(len(hs), max_len)
                j += 1
        return max_len


A = "abcabcbb"

#A = "AaaA"
A = "dadbc"
s = Solution()
print(s.lengthOfLongestSubstring(A))
