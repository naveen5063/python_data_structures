class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        rows = len(A)
        columns = len(A[1])
        column_sum_arr = []
        for i in range(0, columns):
            column_sum = 0
            for j in range(0, rows):
                column_sum += A[j][i]
            column_sum_arr.append(column_sum)
        return column_sum_arr

A = [[1,2,3,4], [5,6,7,8] , [9,2,3,4]]
s = Solution()
s.solve(A)