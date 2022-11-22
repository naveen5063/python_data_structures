class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A > B:
            ans = A - B
        elif B > A:
            ans = B - A
        return ans


A = 1
B = 2
A = 6816621
B = 8157697
# A = 5
# B = 10
A = 4
B = 6
A = 6
B = 7
s = Solution()
print(s.solve(A, B))
