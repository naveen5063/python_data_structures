class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        ans = 1
        for i in range(0, B):
            # ans = (ans*A)%C
            ans = (ans % C * A % C) % C
        return ans % C


A = 2
B = 3
C = 3
s = Solution()
print(s.pow(A, B, C))
