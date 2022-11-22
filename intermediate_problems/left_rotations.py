class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        res = []
        for i in range(0, len(B)):
            if B[i] > len(A):
                ind = B[i] % len(A)
                ans = A[ind:] + A[0:ind]
                res.append(ans)
            else:
                ans = A[B[i]:] + A[0:B[i]]
                res.append(ans)
        return res


A = [1, 2, 3, 4, 5]
B = [2, 3]
s = Solution()
print(s.solve(A, B))
