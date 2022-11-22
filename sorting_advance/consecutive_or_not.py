class Solution:

    def solve(self, A):
        if len(A) == 1:
            return 1
        A.sort()
        for i in range(1, len(A)):
            if A[i] != A[i - 1] + 1:
                return 0
        return 1


A = [3, 2, 1, 4, 5]
A = [1, 3, 2, 5]
s = Solution()
print(s.solve(A))
