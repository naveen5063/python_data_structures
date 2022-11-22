from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # if len(B) == 1:
        #     return True
        adj_list = self.get_adj_list(A, B)
        #print("adj_list", adj_list)
        color_arr = [0] * A
        que = deque()
        for i in range(1, A):
            if color_arr[i] != 0:
                continue
            color_arr[i] = 1
            que.append(i)
            while len(que) > 0:
                ele = que.popleft()
                #print("ele", ele)
                #print("len(adj_list[ele])", len(adj_list[ele]))
                for j in range(0, len(adj_list[ele])):
                    adj_node = adj_list[ele][j]
                    if color_arr[ele] == color_arr[adj_node]:
                        return False
                    if color_arr[adj_node] == 0:
                        color_arr[adj_node] = 3 - color_arr[ele]
                        que.append(adj_node)
        return True

    def get_adj_list(self, A, B):
        adj_list = [[] for i in range(A)]
        for i in range(0, len(B)):
            adj_list[B[i][0]].append(B[i][1])
            adj_list[B[i][1]].append(B[i][0])
        return adj_list


A = 2
B = [[0, 1]]


A = 3
B = [[0, 1], [0, 2], [1, 2]]
# A = 10
# B = [
#   [7, 8],
#   [1, 2],
#   [0, 9],
#   [1, 3],
#   [6, 7],
#   [0, 3],
#   [2, 5],
#   [3, 8],
#   [4, 8]
# ]


s = Solution()
print(s.solve(A, B))
