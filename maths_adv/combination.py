# recursion sol
# if A < B: return 0
# if B == 0: return 1
# a = self.solve(A - 1, B - 1, C)
# b = self.solve(A - 1, B, C)
# return (a + b) % C

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        row = A + 1
        col = B + 1
        matrix = [[0 for col in range(col)] for row in range(row)]
        for i in range(0, col):
            matrix[0][i] = 0
        for j in range(0, row):
            matrix[j][0] = 1

        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] = (matrix[i - 1][j] + matrix[i - 1][j - 1]) % C

        return matrix[row - 1][col - 1]


A = 5
B = 2
C = 13
A = 4
B = 3
A = 41
B = 27
C = 143

s = Solution()
print(s.solve(A, B, C))
