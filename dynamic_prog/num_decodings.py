class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if A == "0":
            return 0
        dp = [0] * (len(A) + 1)
        dp[0] = 1
        dp[1] = 1 if 1 <= int(A[0]) <= 9 else 0
        for i in range(2, len(A) + 1):
            if 1 <= int(A[i - 1]) <= 9:
                dp[i] = dp[i - 1]
            if A[i - 2] == "1":
                dp[i] += dp[i - 2]
            elif A[i - 2] == "2" and 0 <= int(A[i - 1]) <= 6:
                dp[i] += dp[i - 2]
        print("dp", dp)
        return dp[len(A)]


A = "12"
A = "0799733"
s = Solution()
print(s.numDecodings(A))
