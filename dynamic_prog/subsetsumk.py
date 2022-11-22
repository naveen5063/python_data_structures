class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dp = [[-1 for i in range(B + 1)] for j in range(len(A))]
        for j in range(B + 1):
            dp[0][j] = 0
        dp[0][0] = 1
        if A[0] <= B:
            dp[0][A[0]] += 1
        #print(dp)
        for i in range(1, len(A)):
            for j in range(0, B + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i]:
                    dp[i][j] += dp[i][j - A[i]]
        print(dp)
        return dp[len(A) - 1][B]


A = [1, 2, 5]
B = 4
# A = [7, 4, 9, 6, 10, 13, 11, 14]
# B = 22
s = Solution()
print(s.solve(A, B))
