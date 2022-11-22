class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        rows = len(A)
        cols = len(B)
        print(rows, cols)
        dp = [[-1 for i in range(rows)] for j in range(cols)]
        print(dp)
        return self.get_lcs(A, B, rows - 1, cols - 1, dp)

    def get_lcs(self, A, B, i, j, dp):
        if i == -1 or j == -1:
            return 0
        if dp[i][j] == -1:
            if A[i] == B[j]:
                dp[i][j] = 1 + self.get_lcs(A, B, i - 1, j - 1, dp)
            else:
                dp[i][j] = max(self.get_lcs(A, B, i - 1, j, dp), self.get_lcs(A, B, i, j - 1, dp))
        return dp[i][j]


A = "abbcdgf"
B = "bbadcgf"
s = Solution()
print(s.solve(A, B))
