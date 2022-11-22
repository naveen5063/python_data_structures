from collections import deque


# To store matrix cell coordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer

    def solve(self, A, B: Point, C: Point):
        if A[B.x][B.y] != 0 or A[C.x][C.y] != 0:
            print("ret")
            return -1

        rows = len(A)
        cols = len(A[0])
        rowNum = [0, 1, -1, 0]
        colNum = [1, 0, 0, -1]
        val = [3, 2, 4, 1]

        visited = [[[False for k in range(4)]for i in range(cols)] for j in range(rows)]
        visited[B.x][B.y][0] = True
        q = deque()
        s = queueNode(B, 0)
        q.append(s)

        while q:
            cur = q.popleft()
            pt = cur.pt
            print("pt.x", pt.x, pt.y)

            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]
                if pt.x == C.x and pt.y == C.y and A[row][col] == 1:
                    print("A[row][col]", row, col, A[row][col])
                    print("dis")
                    return cur.dist

                if self.isValid(row, col, rows, cols) and A[row][col] == 0 and not visited[row][col][i]:
                    visited[row][col][i] = True
                    adjcel = queueNode(Point(row, col), cur.dist + 1)
                    print("adjcel", adjcel)
                    q.append(adjcel)
        return -1

    def isValid(self, row: int, col: int, rows, cols):
        return (row >= 0) and (row < rows) and (col >= 0) and (col < cols)


A = [[0, 0], [0, 0]]
B = [0, 0]
C = [0, 1]

A = [[0, 0], [0, 1]]
B = [0, 0]
C = [0, 1]

A = [
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]
B = [1, 1]
C = [2, 1]

source = Point(B[0], B[1])
dest = Point(C[0], C[1])
s = Solution()
print(s.solve(A, source, dest))






