import sys
sys.setrecursionlimit(1000000000)
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        val = A+1
        dp = [-1] * val
        #print("dp", dp)
        return self.ways_of_pairs(A, dp)

    def ways_of_pairs(self, A, dp):
        if A == 1 or A == 2:
            return A

        if dp[A] != -1:
            return dp[A]

        dp[A] = (self.ways_of_pairs(A-1, dp) + (A-1) * self.ways_of_pairs(A-2, dp)) % 10003
        return dp[A]


A = 5
A = 60041
s = Solution()
print(s.solve(A))