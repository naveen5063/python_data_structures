import sys

sys.setrecursionlimit(1000000000)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.printall(A, B, 0, 0, [])

    def printall(self, A, B, i, sumk, l):
        if i == len(A):
            if sumk <= 1000 and len(l) == B:
                return 1
            else:
                return 0

        if sumk <= 1000 and len(l) == B:
            return 1

        if sumk > 1000:
            return 0

        c = 0

        sumk += A[i]
        l.append(A[i])
        c += self.printall(A, B, i + 1, sumk, l)
        sumk -= A[i]
        l.pop()
        c += self.printall(A, B, i + 1, sumk, l)
        return c


A = [1, 2, 8]
B = 2
s = Solution()
print(s.solve(A, B))