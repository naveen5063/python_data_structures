class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        for i in range(0, len(A) - 1):
            j = i
            while j >= 0 and A[j] > A[j + 1]:
                # print("j", j, A)
                # print("bf", A[j], A[j + 1])
                A[j], A[j + 1] = A[j + 1], A[j]
                # print(A[j], A[j + 1] )
                j -= 1
        return A


A = [1, 3, 7, 11, 14, 20, 9]
s = Solution()
print(s.solve(A))
