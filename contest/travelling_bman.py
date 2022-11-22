class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        res_arr = []
        for i in range(0, A):
            no_of_subarr = (A - i) * (i + 1)
            res_arr.append(no_of_subarr)
        return res_arr


A = 4
s = Solution()
print(s.solve(A))