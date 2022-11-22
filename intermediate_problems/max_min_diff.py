import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxeven = 1 - sys.maxsize
        minodd = sys.maxsize
        for i in range(0, len(A)):
            if A[i] != 0 and A[i] % 2 == 0:
                if A[i] > maxeven:
                    maxeven = A[i]
            elif A[i] != 0:
                if A[i] < minodd:
                    minodd = A[i]
        return maxeven - minodd


A = [0, 2, 9]
# A = [5, 17, 100, 1]
A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
s = Solution()
print(s.solve(A))