class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        return A % 10 + self.solve(A // 10)


A = 462
#A = 111
A = 83557
s = Solution()
print(s.solve(A))
