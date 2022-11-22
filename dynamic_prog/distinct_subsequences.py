class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):

        rows = len(A)
        cols = len(B)
        print(rows, cols)
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        print(dp)
        res = self.get_lcs(A, B, rows - 1, cols - 1, dp)
        print("dp", dp)
        return res

    def get_lcs(self, A, B, i, j, dp):
        if i == -1 and j == -1:
            return 1
        if j == -1:
            return 1
        if i == -1:
            return 0
        if dp[i][j] == -1:
            if A[i] == B[j]:
                dp[i][j] = self.get_lcs(A, B, i - 1, j, dp) + self.get_lcs(A, B, i - 1, j - 1, dp)
            else:
                dp[i][j] = self.get_lcs(A, B, i - 1, j, dp)
        return dp[i][j]


A = "rabbbit"
B = "rabbit"
A = "abc"
B = "abc"
s = Solution()
print(s.numDistinct(A, B))
