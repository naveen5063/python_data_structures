import sys


def solve(A, B, C):
    n = len(A)
    totalsum = 0
    for i in range(0, len(A)):
        totalsum += A[i]

    dp = [[0 for i in range(totalsum + 1)] for j in range(2)]
    for i in range(1, totalsum + 1):
        dp[0][i] = sys.maxsize
    for i in range(1, n + 1):
        for j in range(0, totalsum + 1):
            a = dp[(i - 1) % 2][j]
            if j >= A[i - 1]:
                a = min(a, dp[(i - 1) % 2][j - A[i - 1]] + B[i - 1])
            dp[i % 2][j] = a

    for j in range(totalsum, -1, -1):
        if dp[n % 2][j] <= C:
            return j


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    pass


A = [6, 10, 12]  # values
B = [10, 20, 30]  # weights
C = 50

# A = [1, 3, 2, 4]
# B = [12, 13, 15, 19]
# C = 10

s = Solution()
print(solve(A, B, C))
