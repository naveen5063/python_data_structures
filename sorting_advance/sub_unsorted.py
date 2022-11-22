import sys


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        start = 0
        end = n - 1

        while start < n - 1 and A[start] <= A[start + 1]:
            start += 1

        while end > 0 and A[end] >= A[end - 1]:
            end -= 1

        if start == n - 1:
            return [-1]

        max_ele_mismatch_subarr = 1 - sys.maxsize
        min_ele_mismatch_subarr = sys.maxsize

        for k in range(start, end + 1):
            max_ele_mismatch_subarr = max(A[k], max_ele_mismatch_subarr)
            min_ele_mismatch_subarr = min(A[k], min_ele_mismatch_subarr)

        l = 0
        r = n - 1
        while A[l] <= min_ele_mismatch_subarr and l <= start:
            l += 1

        while A[r] >= max_ele_mismatch_subarr and r >= end:
            r -= 1

        return [l, r]


A = [1, 3, 2, 4, 5]
# A = [1, 2, 3, 4, 5]
s = Solution()
print(s.subUnsort(A))
