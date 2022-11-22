class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    # def diagonal(self, A):
    #     rows = len(A)
    #     columns = len(A[0])
    #     #arr = []
    #     #upper_diagonal = self.get_upper_diagonals(A, columns, rows)
    #     #lower_diagonal = self.get_lower_diagonals(A, columns, rows)
    #     self.get_upper_diagonals(A, columns, rows)
    #     self.get_lower_diagonals(A, columns, rows)
    #     #arr.append(upper_diagonal)
    #     #arr.append(lower_diagonal)
    #
    # def get_upper_diagonals(self, A, columns, rows):
    #     #upper_diagonal = []
    #     for j in range(0, columns):
    #         new_row = []
    #         x = 0
    #         y = j
    #         while x < rows and y >= 0:
    #             new_row.append(A[x][y])
    #             x += 1
    #             y -= 1
    #         new_row = self.extend_with_zero(new_row, rows)
    #         print(new_row)
    #         #upper_diagonal.append(new_row)
    #     #return upper_diagonal
    #
    # def extend_with_zero(self, new_row, rows):
    #     row = new_row
    #     if len(row) < rows:
    #         val = rows - len(row)
    #         row.extend([0] * val)
    #         return row
    #     else:
    #         return row
    #
    # def get_lower_diagonals(self, A, columns, rows):
    #     #lower_diagonal = []
    #     for i in range(1, rows):
    #         new_row = []
    #         x = i
    #         y = columns - 1
    #         while x < rows and y >= 0:
    #             new_row.append(A[x][y])
    #             x += 1
    #             y -= 1
    #         new_row = self.extend_with_zero(new_row, rows)
    #         print(new_row)
    #         #lower_diagonal.append(new_row)
    #     #return lower_diagonal

    def diagonal(self, A):
        rows = len(A)
        columns = len(A[0])
        arr = []
        for j in range(0, columns):
            new_row = []
            x = 0
            y = j
            while x < rows and y >= 0:
                new_row.append(A[x][y])
                x += 1
                y -= 1
            if len(new_row) < rows:
                val = rows - len(new_row)
                new_row.extend([0] * val)
            print("new row", new_row)
            arr.append(new_row)


        for i in range(1, rows):
            new_row = []
            x = i
            y = columns - 1
            while x < rows and y >= 0:
                new_row.append(A[x][y])
                x += 1
                y -= 1
            if len(new_row) < rows:
                val = rows - len(new_row)
                new_row.extend([0] * val)
            print("new row", new_row)
            arr.append(new_row)
        return arr

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.diagonal(A))

#[1 0 0 ] [2 4 0 ] [3 5 7 ] [6 8 0 ] [9 0 0 ]