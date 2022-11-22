import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return int(math.sqrt(A)) ** 2 == A

A = 4

A = 1001
s = Solution()
print(s.solve(A))