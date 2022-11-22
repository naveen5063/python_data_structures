class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        return (A >> B) << B

A = 25
B = 3

#A = 11001 to 11000
s = Solution()
print(s.solve(A, B))