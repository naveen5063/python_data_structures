class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    # def solve(self, A):
    #     transpose = []
    #     rows = len(A)
    #     columns = len(A[0])
    #     B = [[0 for x in range(rows)] for y in range(columns)]
    #     for i in range(rows):
    #         for j in range(i, rows):
    #             B[i][j] ,B[j][i]= A[j][i] , A[i][j]
    #     # for i in range(rows):
    #     #     for j in range(i, rows):
    #     #         B[i][j] = A[j][i]
    #     return B
    def solve(self,A):
        rows = len(A)
        columns = len(A[0])
        B = [[0 for x in range(rows)] for y in range(columns)]
        # iterate through rows
        for i in range(rows):
            # iterate through columns
            for j in range(columns):
                print(i,j)
                B[j][i] = A[i][j]
                print(B)
        print(B)





A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
A = [[1, 2],
     [4, 5],
     [7, 8]]
# [[1, 4, 7],
#  [2, 5, 8],
# A =[
#   [21, 62, 16, 44, 55, 100, 16, 86, 29],
#   [62, 72, 85, 35, 14, 1, 89, 15, 73],
#   [42, 44, 30, 56, 25, 52, 61, 23, 54],
#   [5, 35, 12, 35, 55, 74, 50, 50, 80],
#   [2, 65, 65, 82, 26, 36, 66, 60, 1],
#   [18, 1, 16, 91, 42, 11, 72, 97, 35],
#   [23, 57, 9, 28, 13, 44, 40, 47, 98]]

s = Solution()
print(s.solve(A))