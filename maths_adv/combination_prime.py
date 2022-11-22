import sys
sys.setrecursionlimit(1000000)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def fact(self, A, C):
        num = A
        factorial = 1
        if A == 1 or A == 0:
            return 1
        else:
            for i in range(1, num + 1):
                factorial = (factorial * i) % C
        return factorial % C

    def pow(self, A, B, C):
        he = pow(A, int(B / 2), C)
        ha = (he % C) * (he % C) % C
        if B % 2 == 0:
            return ha % C
        else:
            return (ha * A) % C

    def solve(self, A, B, C):
        print("par1 A", A)
        par1 = self.fact(A, C) % C
        print("par1", par1)
        print("A - B", A - B)
        par2 = self.fact(A - B, C)
        print("par2 fact", par2)
        par2 = (self.pow(par2, C - 2, C)) % C
        print("par2", par2)
        par3 = self.fact(B, C)
        par3 = (self.pow(par3, C - 2, C)) % C
        print("par3", par3)
        return (par1 * (par2 * par3)) % C


A = 5
B = 2
C = 13
# 10
A = 1
B = 1
C = 1
A = 16
B = 16
C = 8623
A = 43211
B = 17868
C = 1191601
A = 37691
B = 8017
C = 758279
A = 828319
B = 683450
C = 15216931

s = Solution()
print("ans ", s.solve(A, B, C))
