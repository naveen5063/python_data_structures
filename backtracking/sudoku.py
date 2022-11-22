class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, A):
        N = len(A[0])
        self.sudoku(A, N, 0, 0)

    def sudoku(self, A, N, row, col):
        if col == N:
            col = 0
            row += 1

        if row == N:
            return True

        print("A[row][col]", type(A[row][col]))
        if int(A[row][col]) > 0:
            return self.sudoku(A, N, row, col + 1)

        for i in range(0, N):
            if self.isvalid(A, N, row, col, i):
                A[row][col] = i
                self.sudoku(A, row, col)
                A[row][col] = 0

        return False











A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
     "....8..79"]
# A = [[53,.,.,7,.,.,.,.], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]

s = Solution()
s.solveSudoku(A)
