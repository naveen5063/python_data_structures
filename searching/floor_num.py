# greatest ele <= k
import sys


class Solution:
    # @param A : integer
    # @return a list of integers
    def floor_number(self, A, key):
        low = 0
        high = len(A) - 1
        ans = sys.maxsize - 1
        while low <= high:
            mid = int((low + high) / 2)
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                ans = A[mid]
                low = mid + 1
            elif A[mid] > key:
                high = mid - 1
        return ans


A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
B = 5
A = [-5, 2, 3, 4, 9, 10, 11, 14, 18]
B = 5
s = Solution()
print(s.floor_number(A, B))
