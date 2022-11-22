import sys

class Solution:
    # @param A : integer
    # @return a list of integers
    def first_occurence(self, A, key):
        low = 0
        high = len(A) - 1
        ans = sys.maxsize-1
        while low <= high:
            mid = int((low + high) / 2)
            if A[mid] == key:
                ans = mid
                high = mid - 1
            elif A[mid] < key:
                low = mid + 1
            elif A[mid] > key:
                high = mid - 1
        return ans


A = [-5, -5, 3, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 8, 10, 10, 15, 15]
B = 5
s = Solution()
print(s.first_occurence(A, B))