class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        rows = len(A)
        cols = len(B)
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        return self.is_matching(A, B, rows - 1, cols - 1, dp)

    def is_matching(self, A, B, i, j, dp):
        if i == -1 and j == -1:
            return 1
        if j == -1:
            return 0
        if i == -1:
            for i in range(0, j+1):
                if B[i] != "*":
                    return 0
            return 1

        if dp[i][j] == -1:
            if A[i] == B[j] or B[j] == "?":
                dp[i][j] = self.is_matching(A, B, i - 1, j - 1, dp)
            elif B[j] == "*":
                dp[i][j] = self.is_matching(A, B, i, j - 1, dp) or self.is_matching(A, B, i - 1, j, dp)
            else:
                dp[i][j] = 0
        return dp[i][j]

A = "aaa"
B = "a*"

# A = "acz"
# B = "a?a"

A = "bcaccbabaa"
B = "bb*c?c*?"


s = Solution()
print(s.isMatch(A, B))
