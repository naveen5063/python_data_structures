from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        if B == C:
            return 1
        graph_list = [[] for i in range(len(A) + 1)]
        visited = [False for i in range(len(A) + 1)]
        visited[1] = True
        nodepath = [-1 for i in range(len(A) + 1)]
        nodepath[1] = -1
        source_dist_path = []
        graph_queue = deque()
        graph_queue.append(C)

        print("graph_list", graph_list)
        # generate graph adjacency list
        for i in range(1, len(A)):
            graph_list[A[i]].append(i + 1)
            # if undirected
            # graph_list[B[i][1]].append(B[i][0])
        print("graph_list", graph_list)
        while len(graph_queue) > 0:
            cur = graph_queue.pop()
            print("graph_list[cur]", graph_list[cur])
            for i in range(0, len(graph_list[cur])):
                cur_vis = graph_list[cur][i]
                if not visited[cur_vis]:
                    visited[cur_vis] = True
                    graph_queue.append(cur_vis)
                    nodepath[cur_vis] = cur

        print("visited", visited)
        # print("nodepath", nodepath)
        dest = nodepath[B]
        print("des", dest)
        if dest == -1:
            return 0
        while dest != -1:
            source_dist_path.append(dest)
            dest = nodepath[dest]
        return 1


A = [1, 1, 2]
B = 1
C = 2

# A = [1, 1, 2]
# B = 2
# C = 1

# A = [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
# B = 2
# C = 8
# # 0

A = [1, 1, 1, 3, 3, 2, 2, 7, 6]
B = 9
C = 1
# 1

A = [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
B = 6
C = 5
#0

# A = [1, 1, 1, 1, 1]
# B = 1
# C = 1
# # 1
s = Solution()
print(s.solve(A, B, C))
