import sys
from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        x = [-1, +1, 0, 0]
        y = [0, 0, -1, +1]
        rotten_oranges = deque()
        mintime = [[-1 for i in range(M)] for j in range(N)]
        for i in range(N):
            for j in range(M):
                if A[i][j] == 2:
                    rotten_oranges.append([i, j])
                    mintime[i][j] = 0
        #print("rotten_oranges", rotten_oranges)
        while len(rotten_oranges) > 0:
            rotten = rotten_oranges.popleft()
            #print("rotten", rotten)
            i, j = rotten[0], rotten[1]
            for k in range(4):
                a, b = i + x[k], j + y[k]
                if 0 <= a < N and 0 <= b < M and A[a][b] == 1:
                    A[a][b] = 2
                    mintime[a][b] = mintime[i][j] + 1
                    rotten_oranges.append([a, b])
            #print("mintime", mintime)

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    return -1
        mintime_to_rotten = 1 - sys.maxsize


        for i in range(N):
            for j in range(M):
                mintime_to_rotten = max(mintime_to_rotten, mintime[i][j])
        return mintime_to_rotten


A = [[2, 1, 1],
     [1, 1, 0],
     [0, 1, 2]]

# A = [[2, 1, 1],
#      [0, 1, 1],
#      [1, 0, 1]]

A = [
  [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
  [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
  [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
  [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
  [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
  [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
  [2, 2, 0, 2, 2, 1, 1, 1, 2, 2]
]

s = Solution()
print(s.solve(A))
