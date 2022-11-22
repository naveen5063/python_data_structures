class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res = self.get_xor_of_all(A)
        pos = self.get_set_bit_pos(res)
        return self.get_unique_elem(A, pos)

    def get_unique_elem(self, A, pos):
        set_bit = 0
        unset_bit = 0
        ele_arr = []
        for i in range(0, len(A)):
            if self.check_bit(A[i], pos):
                set_bit ^= A[i]
            else:
                unset_bit ^= A[i]
        ele_arr.append(set_bit)
        ele_arr.append(unset_bit)
        ele_arr.sort()
        return ele_arr

    def get_set_bit_pos(self, res):
        pos = 0
        for i in range(0, 32):
            if self.check_bit(res, i):
                pos = i
                break
        return pos

    def get_xor_of_all(self, A):
        res = 0
        for i in range(0, len(A)):
            res ^= A[i]
        return res

    def check_bit(self, A, i):
        return (A >> i) & 1 == 1


A = [1, 2, 3, 1, 2, 4]
s = Solution()
print(s.solve(A))
