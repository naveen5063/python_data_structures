class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        arr = []
        return self.TOH(A, 1, 2, 3, arr)

    def TOH(self, N, S, H, D, arr):
        if N == 0:
            return
        self.TOH(N - 1, S, D, H, arr)
        arr.append([N, S, D])
        self.TOH(N - 1, H, S, D, arr)
        return arr


A = 2
#[1 1 2 ] [2 1 3 ] [1 2 3 ]
s = Solution()
print(s.towerOfHanoi(A))
