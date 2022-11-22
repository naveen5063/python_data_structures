class Solution:
    # @param A : list of list of chars

    def solveSudoku(self, A):
        for i in range(0, 9):
            for j in range(0, 9):
                if A[i][j] != ".":
                    A[i][j] = int(A[i][j])
        self.printsudoku(A, 0)
        return A

    def printsudoku(self, A, index):

        if index == 81:
            return True

        r = int(index / 9)
        c = int(index % 9)

        if A[r][c] != ".":
            return self.printsudoku(A, index + 1)
        else:
            for i in range(1, 10):
                if self.isvalid(A, r, c, i):
                    A[r][c] = int(i)
                    if self.printsudoku(A, index + 1):
                        return True
                    A[r][c] = "."
        return False

    def isvalid(self, A, r, c, d):
        for j in range(0, 9):
            if A[r][j] == d:
                return False
            if A[j][c] == d:
                return False

        x = r - r % 3
        y = c - c % 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if A[i][j] == d:
                    return False

        return True

A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
     "....8..79"]

A = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

s = Solution()
print(s.solveSudoku(A))
