class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0  # no of elements less than B
        min_swap = 0  # no of swaps required
        ans = 1000000000
        n = len(A)
        for i in range(len(A)):
            if A[i] <= B:
                count += 1

        # no of swaps required in first window of size c
        for i in range(count):
            if A[i] > B:
                min_swap += 1
        ans = min(min_swap, ans)

        # now sliding our window to get min swaps
        for i in range(count, n):
            if A[i - count] <= B < A[i]:
                min_swap += 1
            elif A[i - count] > B >= A[i]:
                min_swap -= 1
            ans = min(ans, min_swap)

        return ans


A = [1, 12, 10, 3, 14, 10, 5]
B = 8

s = Solution()
print(s.solve(A, B))
