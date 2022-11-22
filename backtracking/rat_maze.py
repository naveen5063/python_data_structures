class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A[0])
        ratmaze = [[0 for i in range(N)] for j in range(N)]
        self.get_path(A, ratmaze, N, 0, 0)
        return ratmaze

    def get_path(self, maze, ratmaze, N, row, col):

        if row == N - 1 and col == N - 1 and maze[row][col] == 1:
            print("founc", row, col)
            ratmaze[row][col] = 1
            return True

        if row == N or col == N:
            print("row", row, col)
            return False

        if maze[row][col] == 1:
            ratmaze[row][col] = 1

            # proceed moving right
            print("row right", row, col)
            if self.get_path(maze, ratmaze, N, row, col + 1):
                return True

            # proceed moving down
            print("row down", row, col)
            if self.get_path(maze, ratmaze, N, row + 1, col):
                return True
            print("ratmaze[row][col]", row, col, ratmaze[row][col])
            ratmaze[row][col] = 0
        return False


A = [[1, 1, 1],
     [1, 0, 1],
     [0, 0, 1]
     ]

A = [[1, 1, 1],
     [1, 0, 0],
     [1, 1, 1]
     ]
s = Solution()
print(s.solve(A))
