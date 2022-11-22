class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        for i in range(0, 32):
            if self.check_bit(A, i):
                count += 1
        return count

    def check_bit(self, out, i):
        return (out >> i) & 1 == 1


A = 11
s = Solution()
print(s.numSetBits(A))
