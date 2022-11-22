from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # if len(B) == 1:
        #     return True
        freq = [0] * 3
        #print("freq", freq)
        adj_list = self.get_adj_list(A, B)
        #print("adj_list", adj_list)
        color_arr = [0] * (A + 1)
        que = deque()
        for i in range(1, A + 1):
            if color_arr[i] != 0:
                continue
            color_arr[i] = 1
            freq[i] += 1
            que.append(i)
            while len(que) > 0:
                ele = que.popleft()
                #print("ele", ele)
                #print("len(adj_list[ele])", len(adj_list[ele]))
                for j in range(0, len(adj_list[ele])):
                    adj_node = adj_list[ele][j]
                    if color_arr[adj_node] == 0:
                        color_arr[adj_node] = 3 - color_arr[ele]
                        freq[3 - color_arr[ele]] += 1
                        que.append(adj_node)
        #print("freq", freq)
        #print("len(freq)", len(freq))
        total_edges = 1
        for i in range(1, len(freq)):
            total_edges *= freq[i]
        #print("total_edges", total_edges - len(B))
        return (total_edges - len(B))% 1000000007

    def get_adj_list(self, A, B):
        adj_list = [[] for i in range(A + 1)]
        for i in range(0, len(B)):
            #print("B[i][0]", B[i][0], B[i][1])
            adj_list[B[i][0]].append(B[i][1])
            adj_list[B[i][1]].append(B[i][0])
        return adj_list


A = 3
B = [
   [1, 2],
   [1, 3]
 ]

A = 5
B = [
   [1, 3],
   [1, 4],
   [3, 2],
   [3, 5]
 ]

s = Solution()
print(s.solve(A, B))