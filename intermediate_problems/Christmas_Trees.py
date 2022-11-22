import sys


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        if N < 3:
            return -1
        min_sum = sys.maxsize
        mid = 1
        while mid < N - 1:

            s = mid - 1
            left = sys.maxsize
            while s >= 0:
                if A[mid] > A[s]:
                    left = min(B[s], left)
                s -= 1

            e = mid + 1
            right = sys.maxsize
            while e < N:
                if A[mid] < A[e]:
                    right = min(B[e], right)
                e += 1

            total_sum = left + right + B[mid]
            min_sum = min(min_sum, total_sum)
            mid += 1

        if min_sum == sys.maxsize:
            return -1
        return min_sum



A = [1, 3, 5]
B = [1, 2, 3]

A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]

s = Solution()
print(s.solve(A, B))