class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def check_bit_right_shift(self, A, i):
        print(A)
        binval = bin(A)[2:]
        print(binval)
        return (int(binval) >> i) & 1 == 1

    def check_bit_left_shift(self, A, i):
        print(A)
        binval = bin(A)[2:]
        print(binval)
        print((int(binval) << i))
        return (int(binval) << i) & 1 == 1

    def set_bit(self, A, i):
        print(A)
        binval = bin(A)[2:]
        print(binval)
        # return A + (1 << i)
        print(1 << i)
        print(A)
        return A | 1 << i


A = 10
i = 2
s = Solution()
# print(s.check_bit_right_shift(A, i))
# print(s.check_bit_left_shift(A, i))
A = 26
print(s.set_bit(A, 1))
