import sys


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        arrlen = len(A[0])
        dp = [[[sys.maxsize for i in range(arrlen + 1)] for j in range(arrlen + 1)] for k in range(arrlen + 1)]
        for i in range(1, arrlen + 1):
            for j in range(1, arrlen + 1):
                if i == j:
                    dp[i][j][0] = 0
                else:
                    dp[i][j][0] = A[i-1][j-1]
        print(dp)
        for k in range(1, arrlen + 1):
            for i in range(1, arrlen + 1):
                for j in range(1, arrlen + 1):
                    #print("--", min(dp[i][j][k-1], dp[i][k][k - 1] + dp[k][j][k - 1]))
                    dp[i][j][k] = min(dp[i][j][k-1], dp[i][k][k - 1] + dp[k][j][k - 1])
        print(dp)


A = [[0, 50, 39],
     [-1, 0, 1],
     [-1, 10, 0]]
A =[
  [0, 5, -1, 10],
  [-1, 0, 3, -1],
  [-1, -1, 0, 1],
  [-1, -1, -1, 0]
]
s = Solution()
print(s.solve(A))
