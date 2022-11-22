class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        dp = [-1 for i in range(n)]
        palindrome = [[-1 for i in range(n)] for j in range(n)]
        return self.get_partitions(dp, palindrome, A, n - 1, n)

    def isPalindrome(self, text):
        return text == text[::-1]

    def get_partitions(self, dp, palindrome, A, i, N):
        if self.isPalindrome(A[0:i+1]):
            return 1
        if dp[i] == -1:
            ans = N
            for j in range(i - 1, -1, -1):
                if self.isPalindrome(A[j + 1:i+1]):
                    ans = min(ans, self.get_partitions(dp, palindrome, A, j, N) + 1)
            dp[i] = ans
        return dp[i]


A = "aba"
# A = "aab"
# A = "bbdadb"
A = "anaconoaa"
#A = "bananas"
A = "T"
s = Solution()
print(s.minCut(A))
