class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        rows = len(A)
        cols = len(B)
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        return self.get_min_operations(A, B, rows - 1, cols - 1, dp)

    def get_min_operations(self, A, B, i, j, dp):
        if i == -1 and j == -1:
            return 0
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if dp[i][j] == -1:
            if A[i] == B[j]:
                dp[i][j] = self.get_min_operations(A, B, i - 1, j - 1, dp)
            else:
                insert = self.get_min_operations(A, B, i, j - 1, dp)
                delete = self.get_min_operations(A, B, i - 1, j, dp)
                replace = self.get_min_operations(A, B, i - 1, j - 1, dp)
                print(insert, delete, replace)
                dp[i][j] = 1 + min(insert, delete, replace)
        return dp[i][j]


A = "abad"
B = "abac"
A = "Anshuman"
B = "Antihuman"
A = "aaa"
B = "aa"
s = Solution()
print(s.minDistance(A, B))
