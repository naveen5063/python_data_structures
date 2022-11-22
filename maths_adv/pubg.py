class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prev = A[0]
        for i in range(1, len(A)):
            prev = self.get_gcd(prev, A[i])
        return prev

    def get_gcd(self, A, B):
        if B == 0:
            return A
        else:
            return self.get_gcd(B, A % B)


A = [6, 4]
# A = [2, 3, 4]

s = Solution()
print(s.solve(A))
