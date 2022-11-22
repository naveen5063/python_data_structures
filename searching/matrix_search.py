import sys


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    def searchMatrix(self, A, B):
        if len(A) > 1:
            cols = len(A[0]) - 1
            print("cols", len(A))
            ceil_arr = self.column(A, cols)
            print("ceil_arr", ceil_arr)
            ceil_num = self.ceil_number(ceil_arr, B)
            print("ceil_num", ceil_num)
            print("A[ceil_num]", A[ceil_num])
            return self.binary_search(A[ceil_num], B)
        return self.binary_search(A[0], B)

    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def ceil_number(self, A, key):
        low = 0
        high = len(A) - 1
        ans = 0
        print("ans", ans)
        while low <= high:
            mid = int((low + high) / 2)
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                low = mid + 1
            elif A[mid] > key:
                ans = mid
                high = mid - 1
        return ans

    def binary_search(self, A, key):
        print("A", A)
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if A[mid] == key:
                return 1
            elif A[mid] < key:
                low = mid + 1
            elif A[mid] > key:
                high = mid - 1
        return 0


A = [[1, 3, 5, 7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
B = 3
A = [[3, 3, 11, 12, 14],
     [16, 17, 30, 34, 35],
     [45, 48, 49, 50, 52],
     [56, 59, 63, 63, 65],
     [67, 71, 72, 73, 79],
     [80, 84, 85, 85, 88],
     [88, 91, 92, 93, 94]]
B = 94
A = [
  [22, 32, 67]
]
B = 93
#
# A =[[8, 10, 25, 26],
#   [28, 34, 38, 50],
#   [62, 74, 76, 78]]
# B = 95

s = Solution()
print(s.searchMatrix(A, B))
