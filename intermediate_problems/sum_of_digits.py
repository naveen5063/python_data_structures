class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        print(A/10)
        print(A%10)
        return (A % 10 + self.solve(int(A / 10)))

A = 467
s = Solution()
print(s.solve(A))