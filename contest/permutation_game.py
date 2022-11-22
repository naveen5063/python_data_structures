import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        count = 0
        for i in range(0, len(A)):
            count += abs(i + 1 - A[i])
            count %= math.pow(10, 9) + 7
        return int(count)


A = [-1, -1, 2]
s = Solution()
print(s.solve(A))
