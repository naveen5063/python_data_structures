class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        dp = [-1] * len(A[0])
        arr = self.singlearr(A)
        if len(A[0]) == 1:
            return arr[0]
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, len(A[0])):
            dp[i] = max(dp[i - 1], arr[i] + dp[i - 2], arr[i])
        # print("dp", dp)
        # print(dp[len(A[0]) - 1])
        return dp[len(A[0]) - 1]

    def singlearr(self, A):
        arr = [0] * len(A[0])
        for i in range(0, len(A[0])):
            # print("i", i)
            # print(max(A[0][i], A[1][i]))
            arr[i] = max(A[0][i], A[1][i])
        print("Arr", arr)
        return arr


A = [
    [1, 2, 3, 4],
    [2, 3, 4, 5]
]

A = [
    [2, 68],
    [13, 4]
]

A = [
  [28],
  [10]
]
s = Solution()
print(s.adjacent(A))
