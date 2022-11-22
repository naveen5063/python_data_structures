class Solution:
    # @param A : tuple of integers
    # @return an integer

    def check_bit(self, A, i):
        return (A >> i) & 1 == 1

    def singleNumber(self, A):
        ans = 0
        for i in range(0, 30):
            c = 0
            for j in range(0, len(A)):
                if self.check_bit(A[j], i):
                    c += 1

            if c % 3 == 1:
                ans += 1 << i
        return ans

A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
s = Solution()
print(s.singleNumber(A))
