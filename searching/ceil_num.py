# greatest ele >= k
import sys


class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A, B, C):
        low = 0
        high = A - 1
        ans = - 1
        while low <= high:
            mid = int((low + high) / 2)
            print(low, high, mid)
            print("B[mid]", B[mid], C)
            if B[mid] == C:
                print("found", B[mid])
                return B[mid]
            elif B[mid] < C:
                low = mid + 1
            elif B[mid] > C:
                ans = B[mid]
                high = mid - 1
        return ans


A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
B = 5
A = [-5, 2, 3, 4, 9, 10, 11, 14, 18]
B = 5

A = 11
B = [-98, -95, -79, -68, -41, -40, -18, 8, 34, 49, 73]
C = 29

A = 6
B = [3, 7, 9, 11, 19, 20]
C = 22

# A = 5
# B = [2, 5, 6, 9, 18]
# C = 7

# A = 13
# B = [ -95, -88, -85, -57, -53, -37, -29, 1, 23, 31, 56, 74, 99 ]
# C = 1
A = 20
B = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
C = 12

s = Solution()
print(s.solve(A, B, C))
