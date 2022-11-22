class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = A[0]
        for i in range(0, len(A)):
            sum = 0
            for j in range(i, len(A)):
                sum += A[j]
                #print(sum)
                if sum > max_sum:
                    max_sum = sum
        return max_sum

A = [1, 2, 3, 4, -10]
s = Solution()
print(s.maxSubArray(A))