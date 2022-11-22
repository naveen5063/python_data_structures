import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def binary_search(self, A, key):
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = int((low + high) / 2)
            print(low, mid, high)
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                low = mid + 1
            elif A[mid] > key:
                high = mid - 1
        return -1


A = [3, 6, 9, 12, 14, 19, 20, 23, 25, 27]
B = 12

A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12
s = Solution()
print(s.binary_search(A, B))
