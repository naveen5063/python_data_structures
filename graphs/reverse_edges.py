import sys
from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def reverseEdges(self, A, B):
        adj_list = self.get_adj_list(A, B)
        #print("adj", adj_list)
        min_time = [sys.maxsize] * (A + 1)
        blasted = [0] * (A + 1)
        que = deque()
        que.append(1)
        min_time[1] = 0

        while len(que) > 0:
            ele = que.popleft()
            #print("ele", ele)
            if blasted[ele]:
                #print("cont")
                continue
            blasted[ele] = 1
            for i in range(0, len(adj_list[ele])):
                node = adj_list[ele][i][0]
                weight = adj_list[ele][i][1]
                if min_time[node] > min_time[ele] + weight:
                    min_time[node] = min_time[ele] + weight
                    if weight == 0:
                        que.appendleft(node)
                    else:
                        que.append(node)
        #print("min_time", min_time)
        if min_time[A] == sys.maxsize:
            return -1
        return min_time[A]

    def get_adj_list(self, A, B):
        adj_list = [[] for i in range(A + 1)]
        for i in range(0, len(B)):
            adj_list[B[i][0]].append([B[i][1], 0])
            adj_list[B[i][1]].append([B[i][0], 1])
        return adj_list


A = 5
B = [[1, 2],
     [2, 3],
     [4, 3],
     [4, 5]]

# A = 5
# B = [[1, 2],
#      [2, 3],
#      [3, 4],
#      [4, 5]]

A = 6
B = [
  [1, 2],
  [2, 3],
  [3, 4],
  [4, 1],
  [2, 3],
  [4, 2],
  [3, 4],
  [5, 5],
  [5, 5]
]

s = Solution()
print(s.reverseEdges(A, B))
