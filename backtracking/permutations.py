class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res = []
        N = len(A)
        self.get_permute(A, res, N, 0)
        return res

    def get_permute(self, A, res, N, i):
        if i == N - 1:
            res.append(A[:])
            return

        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            self.get_permute(A, res, N, i + 1)
            A[i], A[j] = A[j], A[i]


A = [1, 2, 3]
A = [1, 1, 2]
s = Solution()
print(s.permute(A))
