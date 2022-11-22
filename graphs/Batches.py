class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        adj_edges = self.get_adj_list(A, B, C)
        wei = [0 for i in range(len(B) + 1)]
        for i in range(1, len(B) + 1):
            wei[i] = B[i-1]
        visited = [False] * (A + 1)
        components = 0
        for i in range(1, A + 1):
            if not visited[i]:
                if self.dfs(adj_edges, visited, i, wei[i], wei) >= D:
                    components += 1
        return components

    def dfs(self, adj_list, visited, source, weight, wei):
        if len(adj_list[source]) == 0:
            return weight
        if visited[source]:
            return 0
        visited[source] = True

        for i in range(0, len(adj_list[source])):
            v = adj_list[source][i]
            weight += self.dfs(adj_list, visited, v, wei[v], wei)
        return weight

    def get_adj_list(self, A, B, C):
        adj_list = [[] for i in range(A + 1)]
        for i in range(0, len(C)):
            adj_list[C[i][0]].append(C[i][1])
            adj_list[C[i][1]].append(C[i][0])
        return adj_list


A = 7
B = [1, 6, 7, 2, 9, 4, 5]
C = [[1, 2],
     [2, 3],
     [3, 1],
     [5, 6],
     [5, 7]]
D = 12

A = 5
B = [1, 2, 3, 4, 5]
C = [[1, 5],
     [2, 3]]
D = 6

s = Solution()
print(s.solve(A, B, C, D))
