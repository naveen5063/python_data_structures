class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        total_sum = []
        for i in range(0, len(B)):
            sum = 0
            left = B[i][0]
            right = B[i][1]
            for j in range(left - 1, right):
                sum += int(A[j])
            total_sum.append(sum)
        return total_sum

A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]

A = [2, 2, 2]
B = [[1, 1], [2, 3]]

s = Solution()
print(s.rangeSum(A, B))
