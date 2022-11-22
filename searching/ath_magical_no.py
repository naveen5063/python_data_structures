class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A, B, C):
        low = 1
        high = min(B, C) * A
        ans = 0
        lcm = B * C / self.gcd(B, C)
        while low <= high:
            mid = int((low + high) / 2)
            no_of_multiples = int(mid / B) + int(mid / C) - int(mid / lcm)
            if no_of_multiples < A:
                low = mid + 1
            elif no_of_multiples > A:
                high = mid - 1
            else:
                ans = mid
                high = mid - 1
        return ans % 1000000007

A = 4
B = 2
C = 3
# 6
A = 1
B = 2
C = 3
# 2

s = Solution()
print(s.solve(A, B, C))
