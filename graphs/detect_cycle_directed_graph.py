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

        incoming_edges = [0] * (A + 1)
        for i in range(1, A + 1):
            for j in range(len(adj_mat[i])):
                val = adj_mat[i][j]
                incoming_edges[val] += 1

        minheap = []
        heapify(minheap)
        for i in range(1, A + 1):
            if incoming_edges[i] == 0:
                heappush(minheap, i)

        while len(minheap) > 0:
            node1 = heappop(minheap)
            res.append(node1)
            for i in range(len(adj_mat[node1])):
                node2 = adj_mat[node1][i]
                incoming_edges[node2] -= 1
                if incoming_edges[node2] == 0:
                    heappush(minheap, node2)
        for i in range(0, len(incoming_edges)):
            if incoming_edges[i] > 0:
                return 1
        return 0
        #return incoming_edges

A = 5
B = [  [1, 2],
    [4, 1] ,
    [2, 4] ,
    [3, 4] ,
    [5, 2] ,
    [1, 3] ]

# A = 5
# B = [  [1, 2],
#     [2, 3] ,
#     [3, 4] ,
#     [4, 5] ]

s = Solution()
print(s.solve(A, B))