class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(0, len(A)):
            while 0 < A[i] <= len(A) and A[i] != i+1:
                val = A[i]
                print('val', val)
                if A[i] == A[val-1]:
                    break
                A[val - 1], A[i] = A[i], A[val-1]
        print(A)
        for j in range(0, len(A)):
            if A[j] != j+1:
                return j+1
        return len(A)+1



A = [1, 2, 0]
A = [3, 4, -1, 1]
#A = [-8, -7, -6]
s = Solution()
print(s.firstMissingPositive(A))
