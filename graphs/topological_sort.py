from collections import deque
from heapq import heappop, heappush, heapify
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        res = []
        adj_mat = [[] for i in range(A + 1)]
        for i in range(0, len(B)):
            adj_mat[B[i][0]].append(B[i][1])
        print(adj_mat)

        incoming_edges = [0] * (A + 1)
        for i in range(1, A + 1):
            for j in range(len(adj_mat[i])):
                val = adj_mat[i][j]
                incoming_edges[val] += 1
        print("incoming", incoming_edges)
        sort_queue = deque()
        for i in range(1, A + 1):
            if incoming_edges[i] == 0:
                sort_queue.append(i)
        print("sort_queue", sort_queue)

        while len(sort_queue) > 0:
            node1 = sort_queue.popleft()
            res.append(node1)
            print("node1", node1)
            minheap = []
            heapify(minheap)
            for i in range(len(adj_mat[node1])):
                node2 = adj_mat[node1][i]
                incoming_edges[node2] -= 1
                print("node2 out", node2)
                if incoming_edges[node2] == 0:
                    print("node2", node2)
                    heappush(minheap, node2)
                    #sort_queue.append(node2)
        while minheap:
            print("minheap", minheap)
            val = heappop(minheap)
            sort_queue.append(val)
            res.append(val)
            print("minheap", minheap)

            print("sort_queue in", sort_queue)

        print("reas", res)
A = 6
B = [[6, 3],
     [6, 1],
     [5, 1],
     [5, 2],
     [3, 4],
     [4, 2]]

# A = 3
# B = [[1, 2],
#  [2, 3],
#  [3, 1]]

# A = 8
# B =[
#   [1, 4],
#   [1, 2],
#   [4, 2] ,
#   [4, 3],
#   [3, 2],
#   [5, 2],
#   [3, 5],
#   [8, 2],
#   [8, 6]
# ]

#1 4 3 5 7 8 2 6

s = Solution()
print(s.solve(A, B))