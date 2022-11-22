class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        print("--", A, B)
        if A == 1:
            return 0
        parent = self.solve(A - 1, (B + 1) // 2)
        print("parent", parent, A, B, B % 2)
        if B % 2 == 1:
            print("if ", B, B % 2)
            return parent
        else:
            print("else")
            return 1 - parent


A = 2
B = 1

# A = 2
# B = 2

A = 3
B = 3

s = Solution()
print(s.solve(A, B))
