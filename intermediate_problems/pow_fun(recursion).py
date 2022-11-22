class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        he = pow(A, int(B / 2), C)
        ha = (he % C) * (he % C) % C
        if B % 2 == 0:
            return ha % C
        else:
            return (ha * A) % C


x = 2
n = 3
d = 3

s = Solution()
print(s.pow(x, n, d))
