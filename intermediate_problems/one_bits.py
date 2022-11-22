class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        # bin_val = int(bin(A)[2:])
        # count = 0
        # while (bin_val > 0):
        #     if ((bin_val&1) == 1):
        #         count += 1
        #     bin_val = bin_val >> 1
        #     print(bin_val)
        # return count
        if A & 1 == 0:
            print("its odd")



A = 11
s = Solution()
print(s.numSetBits(A))


