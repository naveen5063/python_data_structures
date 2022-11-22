class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        rows = len(A)
        columns = len(A[0])
        A = self.get_row_pf(A, columns, rows)
        A = self.get_column_pf(A, columns, rows)
        return self.get_sub_matrix_sum(A, B, C, D, E)

    def get_sub_matrix_sum(self, A, B, C, D, E):
        ans = []
        for i in range(0, len(B)):
            a1 = B[i] - 1
            b1 = C[i] - 1
            a2 = D[i] - 1
            b2 = E[i] - 1
            BR1 = 0
            TL1 = 0
            TL = 0
            BR = A[a2][b2]
            if b1 > 0:
                BR1 = A[a2][b1 - 1]
            if a1 > 0:
                TL1 = A[a1 - 1][b2]
            if a1 > 0 and b1 > 0:
                TL = A[a1 - 1][b1 - 1]
            val = BR - BR1 - TL1 + TL
            ans.append(val)
        return ans

    def get_column_pf(self, A, columns, rows):
        for i in range(0, columns):
            for j in range(1, rows):
                A[j][i - 1] = A[j - 1][i - 1] + A[j][i - 1]
        return A

    def get_row_pf(self, A, columns, rows):
        for i in range(0, rows):
            for j in range(1, columns):
                A[i - 1][j] = A[i - 1][j - 1] + A[i - 1][j]
        return A




A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]

A = [[5, 17, 100, 11],
     [0, 0, 2, 8]]
B = [1, 1]
C = [1, 4]
D = [2, 2]
E = [2, 4]

#[12, 28]

s = Solution()
print(s.solve(A, B, C, D, E))