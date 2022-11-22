import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0:
            return 0
        if B == 0:
            return 1
        he = self.pow(A, int(B / 2), C)
        ha = (he % C * he % C) % C
        if B % 2 == 0:
            return ha % C
        else:
            return (ha % C * A % C) % C

        # he = pow(A, int(B / 2), C)
        # ha = (he % C) * (he % C) % C
        # if B % 2 == 0:
        #     return ha % C
        # else:
        #     return (ha * A) % C

A = 2
B = 3
C = 3
# 2
# 2 ^ 3 % 3 = 8 % 3 = 2
A = 0
B = 0
C = 1

s = Solution()
print(s.pow(A, B, C))