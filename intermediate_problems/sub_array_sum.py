class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        total_sum = 0
        len1 = len(A)
        for i in range(0, len1):
            total_sum += (len1 - i) * (i + 1) * A[i]
        return total_sum

A = [1, 2, 3]
s = Solution()
print(s.subarraySum(A))
