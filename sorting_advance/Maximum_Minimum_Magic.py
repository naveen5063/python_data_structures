class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_magic_no = 0
        min_magic_no = 0
        n = len(A)
        A.sort()
        mod = 10 ** 9 + 7
        for i in range(0, n//2):
            max_magic_no = ((max_magic_no % mod ) + (abs(A[n - i - 1] - A[i]) % mod)) % mod
        for i in range(0, n-1, 2):
            min_magic_no = ((min_magic_no % mod ) + (abs(A[i + 1] - A[i]) % mod)) % mod

        return [max_magic_no, min_magic_no]


A = [3, 11, -1, 5]
s = Solution()
print(s.solve(A))