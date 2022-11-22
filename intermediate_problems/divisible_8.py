class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        num = int(A)%1000
        if num % 8 == 0:
            return 1
        else:
            return 0
A = 16
A = 342024
A = 184778
s = Solution()
print(s.solve(A))