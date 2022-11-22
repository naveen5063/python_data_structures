import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # TC N2
        # avg = sys.maxsize
        # index = -1
        # for i in range(0, len(A)):
        #     subsum = 0
        #     for j in range(i, B + i):
        #         if j < len(A) and i <= len(A) - B:
        #             subsum += A[j]
        #     if subsum != 0 and subsum < avg:
        #         avg = subsum
        #         index = i
        # return index

        minaverage = float("inf")
        index = -1
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        print(A)
        for i in range(B - 1, len(A)):
            if i == B - 1:
                if A[i] / B < minaverage:
                    minaverage = A[i] / B
                    index = i - B + 1
            else:
                if (A[i] - A[i - B]) / B < minaverage:
                    minaverage = (A[i] - A[i - B]) / B
                    index = i - B + 1
        return index


A = [3, 7, 90, 20, 10, 50, 40]
B = 3

# A = [3, 7, 5, 20, -10, 0, 12]
# B = 2

s = Solution()
print("ans", s.solve(A, B))
