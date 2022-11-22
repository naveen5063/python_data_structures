class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dp = [[-1 for i in range(len(A) + 1)] for j in range(len(A) + 1)]
        print("dp", dp)
        return self.lps(A, 0, len(A) - 1, dp)

    def lps(self, A, i, j, dp):
        print("i", i, j)
        if i <= 0 or j <= 0:
            return 0

        if dp[i][j] == -1:
            print("dp[i][j]", dp[i][j])
            if A[i] == A[j]:
                dp[i][j] = self.lps(A, i + 1, j - 1, dp) + 2
            else:
                dp[i][j] = max(self.lps(A, i, j - 1, dp), self.lps(A, i + 1, j, dp))
        print("dp", dp)
        return dp[i][j]

A = "bebeeed"
A = "aedsead"
s = Solution()
print(s.solve(A))
