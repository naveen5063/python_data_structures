class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        columns = len(A[0])
        arr = []
        for i in range(0, rows):
            row_list = []
            for j in range(0, columns):
                ele_sum = A[i][j] + B[i][j]
                row_list.append(ele_sum)
            arr.append(row_list)
        return arr


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

A =[  [6] ,[2] ,[3] , [10] ,[1] ,[3] ]
B =[[6] ,[7] , [3] ,[8] ,[1] ,[2]]
s = Solution()
print(s.solve(A, B))

#[12 ] [9 ] [6 ] [18 ] [2 ] [5 ]

[[12], [9], [6], [18], [2], [5]]