class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        edges = len(B)
        if edges >= A:
            return 1
        adj_edges = self.get_components(A, B)
        visited = [False] * (A + 1)
        components = 0
        print("adj_edges", adj_edges)
        for i in range(1, A + 1):
            if not visited[i]:
                self.dfs(adj_edges, visited, i)
                components += 1
        print("components", components, (A - components))
        if edges > A - components:
            return 1
        else:
            return 0

    def dfs(self, adj_list, visited, source):
        if visited[source]:
            return
        visited[source] = True
        for i in range(0, len(adj_list[source])):
            v = adj_list[source][i]
            self.dfs(adj_list, visited, v)

    def get_components(self, A, B):
        adj_list = [[] for i in range(A + 1)]
        for i in range(0, len(B)):
            adj_list[B[i][0]].append(B[i][1])
            adj_list[B[i][1]].append(B[i][0])
        return adj_list


A = 5
B = [[1, 2],
     [1, 3],
     [2, 3],
     [1, 4],
     [4, 5]
     ]

A = 3
B = [[1, 2],
     [1, 3]
     ]


A = 68
B =[
  [26, 43],
  [5, 40],
  [23, 35],
  [21, 59],
  [29, 42],
  [6, 15],
  [6, 24],
  [15, 40],
  [13, 15],
  [1, 48],
  [27, 39],
  [9, 42],
  [49, 67],
  [40, 58],
  [47, 54],
  [2, 10],
  [45, 59],
  [2, 8],
  [14, 27],
  [40, 57],
  [13, 58],
  [2, 46],
  [52, 57],
  [8, 21],
  [22, 60],
  [4, 49],
  [33, 49],
  [30, 64],
  [12, 43],
  [7, 41],
  [16, 67],
  [24, 53],
  [10, 12],
  [6, 46],
  [9, 19],
  [19, 41],
  [35, 41],
  [64, 65],
  [50, 60],
  [3, 7],
  [28, 64],
  [49, 51],
  [12, 28],
  [10, 40],
  [3, 36],
  [8, 9],
  [17, 54],
  [9, 30],
  [1, 59],
  [29, 62],
  [16, 39],
  [7, 44],
  [42, 66],
  [2, 33],
  [11, 39],
  [12, 16],
  [22, 65],
  [11, 62],
  [7, 31],
  [15, 32],
  [21, 38],
  [23, 41],
  [21, 52],
  [25, 57]
]

A = 2
B =[
  [1, 2]
]

s = Solution()
print(s.solve(A, B))
