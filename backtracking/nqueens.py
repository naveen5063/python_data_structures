class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        res = []
        mat = [[0 for i in range(A)] for j in range(A)]
        self.print_n_queens_mat(mat, A, 0, res)
        return res

    def print_n_queens_mat(self, mat, A, i, res):
        if i == A:
            res.append(self.printmat(mat))
            return

        for j in range(0, A):
            if self.check(mat, i, j, A):
                mat[i][j] = 1
                self.print_n_queens_mat(mat, A, i + 1, res)
                mat[i][j] = 0

    def check(self, mat, i, j, N):
        for r in range(0, i):
            if mat[r][j] == 1:
                return False

        r = i
        c = j
        while r >= 0 and c >= 0:
            if mat[r][c] == 1:
                return False
            r -= 1
            c -= 1

        r = i
        c = j
        while r >= 0 and c < N:
            if mat[r][c] == 1:
                return False
            r -= 1
            c += 1
        return True

    def printmat(self, mat):
        l = []
        for p2 in mat:
            s = ""
            for val in p2:
                if val == 1:
                    s += "Q"
                else:
                    s += "."
            l.append(s)
        return l


A = 4
s = Solution()
print(s.solveNQueens(A))
