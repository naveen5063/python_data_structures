class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        mod = 1000000007
        n = len(A)
        max_sum = 0
        min_sum = 0

        for index in range(n):
            max_sum += A[index] * ((1 << index) % mod)
            min_sum += A[index] * ((1 << n - 1 - index) % mod)

        return (max_sum - min_sum) % mod


A = [1, 2]

A = [1]
s = Solution()
print(s.solve(A))
