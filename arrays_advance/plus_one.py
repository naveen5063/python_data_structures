class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = self._get_single_num(A)
        num_plus_one = num + 1
        return list(map(int, str(num_plus_one)))

    def _get_single_num(self, A):
        n = ''.join(map(str, A))
        return int(n)


A = [1, 2, 3]
s = Solution()
print(s.plusOne(A))
