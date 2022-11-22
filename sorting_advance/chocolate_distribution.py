import sys


class Solution:

    def solve(self, A, B):
        if B == 0:
            return 0
        if not A:
            return 0

        A.sort()
        n = len(A)
        mindiff = sys.maxsize
        for i in range(n - B + 1):
            diff = A[i + B - 1] - A[i]
            mindiff = min(mindiff, diff)
        return mindiff


A = [3, 4, 1, 9, 56, 7, 9, 12]
B = 5
s = Solution()
print(s.solve(A, B))