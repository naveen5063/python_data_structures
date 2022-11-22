class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        val = self.sum_value(A)
        if len(str(val)) == 1:
            if val == 1:
                return 1
        else:
            return self.solve(val)
        return 0

    def sum_value(self, A):
        if A == 0:
            return 0
        else:
            return A % 10 + self.sum_value(int(A / 10))


A = 83557
A = 1291
s = Solution()
print(s.solve(A))