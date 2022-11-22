# def minFallingPathSum(self, grid: List[List[int]]) -> int:
#     m, n = len(grid), len(grid[0])
#
#     def get_min(i, j):
#         nonlocal n
#         old_val = grid[i - 1][j]
#         grid[i - 1][j] = float('inf')
#         min_val = min(grid[i - 1])
#         grid[i - 1][j] = old_val
#         return min_val
#
#     for i in range(1, m):
#         for j in range(0, n):
#             grid[i][j] = grid[i][j] + get_min(i, j)
#
#     return min(grid[m - 1])

class Solution:
    def minFallingPathSum(self, A):
        n = len(A)
        dp = [[-1 for c in range(n)] for r in range(n)]
        for c in range(n):
            dp[0][c] = A[0][c]

        for r in range(1, n):
            for c in range(n):
                if c == 0:
                    dp[r][c] = A[r][c] + min(dp[r - 1][1:])
                elif c == n - 1:
                    dp[r][c] = A[r][c] + min(dp[r - 1][:n - 1])
                else:
                    min_left = min(dp[r - 1][:c])
                    min_right = min(dp[r - 1][c + 1:])
                    dp[r][c] = A[r][c] + min(min_left, min_right)
        return min(dp[-1])


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s = Solution()
print(s.minFallingPathSum(A))