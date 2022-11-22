class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(0, len(A)):
            ans = ans ^ A[i]
        return ans

A = [1, 2, 2, 3, 1]
s = Solution()
print(s.singleNumber(A))