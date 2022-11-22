class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = A[0][0]
        for st in range(0, B):
            sum = [0] * B
            for end in range(st, B):
                for i in range(0, B):
                    sum[i] += A[end][i]
                print(sum)
                ans = max(ans, self.maxSubArray(sum, B))
        return ans

    def maxSubArray(self, A, size):
        sum = 0
        max_subarr_sum = A[0]
        for i in range(0, size):
            sum += A[i]
            max_subarr_sum = max(sum, max_subarr_sum)
            if sum < 0:
                sum = 0
        return max_subarr_sum


A = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 8, 6, 7, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]
B = 3

# Maximum
# sum3x3
# matrix is
# 8 6 7
# 4 4 4
# 5 5 5
# Sum = 48
s = Solution()
print(s.solve(A, B))