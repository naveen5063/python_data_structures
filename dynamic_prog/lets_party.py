class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        a = 1
        b = 2
        c = b
        for i in range(3, A + 1):
            c = b + (i - 1) * a
            a = b
            b = c
        return c % 10003


A = 5
s = Solution()
print(s.solve(A))
