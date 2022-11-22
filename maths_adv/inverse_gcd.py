class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(0, B):
            print("A * i", A * i, (A * i) % B)
            if (A * i) % B == 1:
                return i


A = 3
B = 5
# Let 's say A-1 mod B = X, then (A * X) % B = 1.
# 3 * 2 = 6, 6 % 5 = 1.
A = 6
B = 23
A = 7
B = 22
s = Solution()
print(s.solve(A, B))
