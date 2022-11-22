class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        print("ab", A, B)
        print("b", B)
        if A == 1 or B == 1:
            return 0
        pre = self.solve(A - 1, int((B + 1) / 2))
        print("pre", pre)
        print("b", B)
        print("b1", (B & 1))
        if pre == 0:
            if (B & 1) == 1:
                return 0
            else:
                return 1
        else:
            if (B & 1) == 1:
                return 1
            else:
                return 0


A = 3
B = 3
#
# Row1: 0
# Row2: 01
# output : 0
s = Solution()
print(s.solve(A, B))