class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        while len(str(A)) > 1:
            A = self.get_sum(A)
        if A == 1:
            return 1
        return 0

    def get_sum(self, A):
        if A == 0:
            return 0
        return A % 10 + self.get_sum(A // 10)

A = 83557
#A = 1291
# Sum of digits of (83557) = 28
# Sum of digits of (28) = 10
# Sum of digits of (10) = 1.
# Single digit is 1, so it's a magic number. Return 1.
s = Solution()
print(s.solve(A))
