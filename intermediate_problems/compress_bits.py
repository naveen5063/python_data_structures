class Solution:
    # @param A : list of integers
    # @return an integer
    def compressBits(self, A):
        ans = 0
        for i in range(0, len(A)):
            ans = ans ^ A[i]
        return ans

A = [1, 3, 5]
s = Solution()
print(s.compressBits(A))