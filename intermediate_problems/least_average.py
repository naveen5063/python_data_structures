
import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        least_avg = sys.maxsize
        for i in range(0, len(A)):
            sum_avg = 0
            for j in range(0, B):
                print("------")
                print(A[j])
                sum_avg += A[j]
                print(sum_avg)
            sum_avg /= B
            least_avg = int(min(least_avg, sum_avg))
        return least_avg


A=[3, 7, 90, 20, 10, 50, 40]
B=3
s = Solution()
print(s.solve(A, B))