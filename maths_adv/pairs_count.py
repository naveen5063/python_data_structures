class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_arr = {}
        mod = 1000000007
        for i in range(0, len(A)):
            val = A[i] % B
            if val in freq_arr:
                freq_arr[val] += 1
            else:
                freq_arr[val] = 1

        c = self.get_pairs(B, freq_arr)
        return int(c % mod)

    def get_pairs(self, B, freq_arr):
        c = 0
        if 0 in freq_arr.keys():
            x = freq_arr[0]
            c += int(x * (x - 1) / 2)
        if int(B % 2) == 0:
            if int(B / 2) in freq_arr.keys():
                x = freq_arr[int(B / 2)]
                c += int(x * (x - 1) / 2)
        for i in range(1, int((B + 1) / 2)):
            if i in freq_arr.keys() and B - i in freq_arr.keys():
                c = c + freq_arr[i] * freq_arr[B - i]
        return c


A = [1, 2, 3, 4, 5]
B = 2
#A = [2,3,4,2,0,3,5,0,5,1,0,4,3,4,3]
#B = 6
A = [ 5, 17, 100, 11 ]
B = 28
# (1, 3), (1, 5), (2, 4), (3, 5)
# 4 pairs
s = Solution()
print(s.solve(A, B))
