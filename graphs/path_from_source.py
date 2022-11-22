from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph_list = [[] for i in range(A + 1)]
        visited = [False for i in range(A + 1)]
        visited[1] = True
        nodelevel = [-1 for i in range(A + 1)]
        nodelevel[1] = 0
        nodepath = [-1 for i in range(A + 1)]
        nodepath[1] = -1
        source_dist_path = []
        graph_queue = deque()
        graph_queue.append(1)

        # generate graph adjacency list
        for i in range(0, len(B)):
            graph_list[B[i][0]].append(B[i][1])
            # if undirected
            # graph_list[B[i][1]].append(B[i][0])

        while len(graph_queue) > 0:
            cur = graph_queue.pop()
            for i in range(0, len(graph_list[cur])):
                cur_vis = graph_list[cur][i]
                if not visited[cur_vis]:
                    visited[cur_vis] = True
                    graph_queue.append(cur_vis)
                    nodepath[cur_vis] = cur
                    nodelevel[cur_vis] = nodelevel[cur] + 1

        dest = nodepath[A]
        if dest == -1:
            return 0
        while dest != -1:
            source_dist_path.append(dest)
            dest = nodepath[dest]
        return 1


A = 5
B = [[1, 2],
     [4, 1],
     [2, 4],
     [3, 4],
     [5, 2],
     [1, 3]]

A = 5
B = [[1, 2],
     [2, 3],
     [3, 4],
     [4, 5]]

s = Solution()
print(s.solve(A, B))
