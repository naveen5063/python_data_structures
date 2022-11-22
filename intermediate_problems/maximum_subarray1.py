class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        total_sum = 0
        for i in range(0, A):
            sum = 0
            for j in range(i, A):
                sum += C[j]
                if sum <= B:
                    total_sum = max(sum, total_sum)
        return total_sum


# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]
A = 3
B = 1
C = [2, 2, 2]

s = Solution()
print(s.maxSubarray(A, B, C))
