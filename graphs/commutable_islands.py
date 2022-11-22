import sys
from heapq import heappop, heappush, heapify


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B):
        adj_mat = self.get_adj_list(A, B)
        min_time = [sys.maxsize] * (A + 1)
        min_time[1] = 0
        min_heap = []
        heapify(min_heap)
        heappush(min_heap, [0, 1])

        while len(min_heap) > 0:
            node = heappop(min_heap)
            node_time = node[0]
            node_data = node[1]
            if node_time > min_time[node_data]:
                continue
            for i in range(0, len(adj_mat[node_data])):
                ele = adj_mat[node_data][i]
                val = ele[0]
                weight = ele[1]
                if node_time + weight < min_time[val]:
                    min_time[val] = node_time + weight
                    heappush(min_heap, [min_time[val], val])
        for i in range(len(min_time)):
            if min_time[i] == sys.maxsize:
                min_time[i] = -1

        return min_time

    def get_adj_list(self, A, B):
        adj_list = [[] for i in range(A + 1)]
        for i in range(0, len(B)):
            adj_list[B[i][0]].append([B[i][1], B[i][2]])
            adj_list[B[i][1]].append([B[i][0], B[i][2]])
        return adj_list


A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]
s = Solution()
print(s.solve(A, B))
