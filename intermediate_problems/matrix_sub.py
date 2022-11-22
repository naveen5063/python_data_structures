class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        #matrix_out =[]
        rows = len(A)
        columns = len(A[0])
        for i in range(rows):
            row = []
            val = 0
            for j in range(columns):
                val = A[i][j] - B[i][j]
                row.append(val)
            #matrix_out.append(row)
            print(row)


A = [[1, 1]]
B = [[2, 3]]

A = [[10], [10]]
B = [[9], [-4]]

# A =[[-5, 7],
#     [3, 1],
#     [4, -10]]
# B = [[3, 4],
#      [2, 3],
#      [10, 1]]


s = Solution()
s.solve(A, B)
