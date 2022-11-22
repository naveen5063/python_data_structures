class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A):
        for i in range(0, len(A)):
            count = 0
            for j in range(0, len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    count += 1
            if count == 0:
                break
        return A


A = [2, 8, 4, -1, 7, 10, 5, 6]
s = Solution()
print(s.solve(A))
