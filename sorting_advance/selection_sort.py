class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A):
        for i in range(0, len(A)):
            minval = A[i]
            minindex = i
            for j in range(i, len(A)):
                if A[j] < minval:
                    minval = A[j]
                    minindex = j
            A[i], A[minindex] = A[minindex], A[i]
        return A


A = [2, 8, 4, -1, 7, 10, 5, 6]
s = Solution()
print(s.solve(A))
