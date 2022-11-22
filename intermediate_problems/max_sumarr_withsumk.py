class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        sum = 0
        for i in range(0, B):
            sum += A[i]
        start = 1
        end = B
        ans = sum
        while start <= len(A) - B:
            sum = sum - A[start - 1] + A[end]
            ans = max(ans, sum)
            start += 1
            end += 1
        return ans


A = [1, 2, 3, 4, 5]
B = 3
A = [-3, 4, -2, 5, 3, -2, 8, 2, 1, 4]
B = 6
s = Solution()
print(s.solve(A, B))
