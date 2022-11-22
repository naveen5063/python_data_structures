class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        dp = [-1 for j in range(A + 1)]
        if A == 1:
            return 1

        dp[1] = 1
        dp[2] = 2
        # a = 1
        # b = 2
        for i in range(3, A + 1):
            dp[i] = dp[i - 1] + dp[i - 2] * (i-1)
            # c = b * a + 1 * b
            # a = b
            # b = c
        # return dp[A] % 10003
        return dp[A] % 10003


A = 5
A = 60041
s = Solution()
print(s.solve(A))
