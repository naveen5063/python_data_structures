class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = 0
        max_subarr_sum = A[0]
        for i in range(0, len(A)):
            sum += A[i]
            max_subarr_sum = max(sum, max_subarr_sum)
            if sum < 0:
                sum = 0
        return max_subarr_sum



A = [1, 2, 3, 4, -10]
s = Solution()
print(s.maxSubArray(A))