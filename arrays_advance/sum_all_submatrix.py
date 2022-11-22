class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        columns = len(A[0])
        ans = 0
        for i in range(0, rows):
            for j in range(0, columns):
                ans = ans + A[i][j] * (i+1) * (j+1) * (rows-i) * (columns-j)
        return ans

A = [[1, 1],
     [1, 1]]
s = Solution()
print(s.solve(A))