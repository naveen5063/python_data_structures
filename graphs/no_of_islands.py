class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count_of_islands = 0
        N = len(A)
        M = len(A[0])
        x = [-1, 1, 0, 0, -1, 1, -1, 1]
        y = [0, 0, -1, 1, -1, 1, 1, -1]
        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    count_of_islands += 1
                    self.dfs(A, i, j, N, M, x, y)

        return count_of_islands

    def dfs(self, A, i, j, N, M, x, y):

        if i < 0 or j < 0 or i >= N or j >= M or A[i][j] == 0:
            return

        A[i][j] = 0
        for k in range(8):
            self.dfs(A, i + x[k], j + y[k], N, M, x, y)


A = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

# A = [
#        [1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [1, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0],
#        [1, 0, 1, 0, 1]
#      ]
s = Solution()
print(s.solve(A))