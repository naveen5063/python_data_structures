class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) <= 2:
            return 1
        A.sort()
        diff = abs(A[1] - A[0])
        print(diff)
        for i in range(2, len(A)):
            print(i)
            temp = A[i] - A[i-1]
            print(temp)
            if temp != diff:
                return 0
        return 1

A = [3, 5, 1]
A = [2, 4, 1]
A = [ -113, -70, -14, -8, -29, 5, -94, -44, 23, 9, 13, -132, -14 ]

s = Solution()
print(s.solve(A))