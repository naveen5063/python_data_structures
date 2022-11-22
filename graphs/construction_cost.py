class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        ans = 0
        # B.sort(reverse=True)
        B.sort(key=lambda x: x[2])
        print(B)
        component = [0 for i in range(A + 1)]
        for i in range(A + 1):
            component[i] = i
        # print(component)
        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]
            w = B[i][2]
            cu = self.findcomponent(component, u)
            cv = self.findcomponent(component, v)
            if cu != cv:
                component[max(cu, cv)] = component[min(cu, cv)]
                ans += w
        return ans

    def findcomponent(self, component, s):
        if component[s] == s:
            return s
        component[s] = self.findcomponent(component, component[s])
        return component[s]


A = 3
B = [[1, 2, 14],
     [2, 3, 7],
     [3, 1, 2]]

A = 3
B = [[1, 2, 20],
     [2, 3, 17]]

A = 4
B = [
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 1],
    [1, 3, 8],
    [1, 4, 12]
]

A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]

A = 4
B = [[1, 2, 1],
     [2, 3, 2],
     [3, 4, 4],
     [1, 4, 3]]
s = Solution()
print(s.solve(A, B))
