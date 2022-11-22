class Solution:
    # @param A : integer
    # @return an integer

    def check_bit(self, A, i):
        return (A >> i) & 1 == 1

    def numSetBits(self, A):
        c = 0
        for i in range(0, 32):
            if self.check_bit(A, i):
                c += 1
        return c


A = 11
s = Solution()
print(s.numSetBits(A))
