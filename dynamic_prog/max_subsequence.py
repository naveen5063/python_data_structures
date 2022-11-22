class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dp = [-1] * int(A+1)
        dp[0] = 1
        for i in range(1, A + 1):
            s = 0
            j = 1
            while j <= 6 and j <= i:
                s += dp[i-j]
                j += 1
            dp[i] = s
        return dp[A]


A = 3
s = Solution()
print(s.solve(A))