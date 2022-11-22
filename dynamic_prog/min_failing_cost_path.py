import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        val = sys.maxsize
        print(rows, cols)
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        print(dp)
        for i in range(0, len(A)):
            dp[0][i] = A[0][i]
        print(dp)
        # for i in range(1, cols+1):
        #     print("rows - i, cols - i", rows - 1, cols - i)
        #     ans = self.get_min_path(A, dp, rows, cols, rows - 1, cols - i)
        #     print("ans", ans)
        #     val = min(val, ans)
        # return val
        self.get_min_path(A, dp, rows, cols, rows - 1, cols - 1)

    def get_min_path(self, A, dp, rows, cols, i, j):
        #print("dp[i bf", i, j, dp[i][j])
        if i < 0 or j < 0:
            return sys.maxsize

        # for i in range(rows):
        #
        # return dp[i][j]

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s = Solution()
print(s.solve(A))
